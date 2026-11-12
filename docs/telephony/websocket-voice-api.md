# WebSocket voice API

For businesses and contact centers that run their **own telephony backend**, for example a
Genesys AudioConnector, a custom PBX bridge or an in-house call platform. Your backend
registers each call with Newo, then streams the caller's audio over a WebSocket and plays the
agent's audio back.

This needs a developer and a backend service. It is not the right path for a single business
without its own telephony system: use [forwarding or SIP](connect-existing-number.md) instead.

## 1. Prerequisites

You need:
- A voice connector whose provider is `websocket`, and its connector ID.
- The WebSocket API key of that connector. Each connector has its own key, not a shared account
  key.
- The caller's phone number. Optionally, your own external call ID.
- For call transfers: `websocket_webhook` (your backend URL that receives transfer requests) and
  `websocket_webhook_api_key` (Newo sends it in the `x-api-key` header), configured on the same
  connector.

## 2. Base URL and authentication

All requests go to `https://apps.newo.ai`, with `Authorization: Bearer <connector_api_key>`.

The key must belong to the connector in `connectorId`:
- a missing or malformed header returns `401`;
- a key of another connector returns `401`;
- an unknown connector returns `404`.

## 3. Register a call

```http
POST /api/v1/websocket-provider/call
Content-Type: application/json
Authorization: Bearer <connector_api_key>
```

```json
{
  "connectorId": "b3f1c2a0-1234-4a5b-9c1d-abcdef012345",
  "genesysCallId": "external-call-123",
  "customer": { "number": "+12345678913" },
  "transport": {
    "provider": "newo.websocket",
    "audioFormat": { "format": "pcm_s16le", "container": "raw", "sampleRate": 16000 }
  }
}
```

| Field | Description |
|---|---|
| `connectorId` | your voice connector ID (alias `assistantId`) |
| `genesysCallId` | optional external call ID (aliases `callId`, `externalCallId`); generated if omitted; it is the call's session key |
| `customer.number` | required; the caller's number |
| `transport.provider` | must be `"newo.websocket"` |
| `transport.audioFormat` | `pcm_s16le` at `16000` Hz, or `mulaw` at `8000` Hz; `container` must be `"raw"` |

A missing required field returns `422`. Response (`200`):

```json
{
  "id": "external-call-123",
  "type": "newo.websocketCall",
  "status": "queued",
  "transport": {
    "provider": "newo.websocket",
    "websocketCallUrl": "wss://apps.newo.ai/api/v1/websocket-provider/external-call-123/transport"
  }
}
```

## 4. Stream the call

Open a WebSocket to `transport.websocketCallUrl`. It needs no query parameters: the audio format
and the caller come from the registration.

- Send the caller's raw audio as binary messages.
- You receive the agent's audio as binary messages.
- Text messages are control frames.

## 5. End the call

From your side, send a text frame:

```json
{ "type": "hangup", "reason": "user hung up" }
```

(`"end-call"` is also accepted.) The server may send `{"type": "end-call", "reason": "assistant-ended-call"}`.
When it does, stop streaming and close the socket.

## 6. Audio formats

| Format | Container | Sample rate | Encoding |
|---|---|---:|---|
| `pcm_s16le` | `raw` | 16000 | 16-bit signed little-endian PCM |
| `mulaw` | `raw` | 8000 | G.711 μ-law |

The format in the registration must match the audio you send.

## 7. Call transfer

When the agent decides to transfer, Newo first calls your webhook:

```http
POST <websocket_webhook>
Content-Type: application/json
x-api-key: <websocket_webhook_api_key>
```

- **Request body:** the call context the agent attached. It is not a fixed schema. Typically it
  has `transcriptSummary`, `callerIntent`, `sentiment` and fields of your use case. If the context
  is missing or invalid, Newo sends `{}`.
- **Your response:** any `2xx` means the transfer was accepted, and Newo sends `{"type": "transfer"}`
  on the call socket. Treat it like `end-call` and route the call on your side.
- **Failure:** any other status, an error, or a webhook that is not configured. Then no `transfer`
  frame is sent, the call continues with the agent, and the agent is not told the transfer failed.

## Notes for coding assistants

- Building the bridge is backend work. Build it and test it in the business's own test environment
  first. Never put the connector key or webhook key in client-side code or in a repository.
- If the business's phone system documents an audio-streaming interface (for example Genesys
  AudioConnector), map its audio format to one of the two formats above, and its transfer
  mechanism to the webhook.
