# Attribute index

Every Customer and Project Attribute of the NAF agent, grouped as in the Newo portal.
Columns: IDN, title (the [A]/[B]/[C] mark is the setup tier: A = basic, B = common,
C = advanced; [IMPORTANT] marks attributes that change behavior a lot), level, value type.
Open the group page for the full description, examples and dependencies.

## 1. Business

Full descriptions: [1-business.md](1-business.md)

- `project_business_name` | 1-01-A. Business Name [A] | Customer | string
- `project_business_name_phonetic` | 1-01-B. Business Phonetic Name [B] | Customer | string
- `project_business_address` | 1-02. Business Address [A] | Customer | string
- `project_business_country` | 1-02-A. Business Country [A] | Customer | string
- `project_business_public_phone` | 1-03. Business Phone (Public Phone) [A] | Customer | string
- `project_business_story` | 1-04. Business Description [A] | Customer | string
- `project_business_website_url` | 1-05. Business Website Link (URL) [A] | Customer | string
- `project_business_working_hours` | 1-06. Working Hours [A] [IMPORTANT] | Customer | string
- `project_business_time_zone` | 1-07. Business Time Zone [A] [IMPORTANT] | Customer | enum
- `project_attributes_payment_methods` | 1-08. Payment Methods [A] | Customer | string
- `project_business_top_owner_name` | 1-09. Billing Manager Full Name [A] | Customer | string
- `project_business_top_owner_phone` | 1-10. Billing Manager Phone Number [A] | Customer | string
- `project_business_top_owner_email` | 1-11. Billing Manager Email [A] | Customer | string
- `project_attributes_setting_common_phone_numbers` | 1-12. Common (Shared) Phone Numbers [A] | Customer | json
- `project_attributes_info_crm` | 1-13. CRM [A] | Customer | string
- `project_business_expected_number_of_calls_month_location` | 1-14. Estimated Monthly Calls [A] | Customer | number
- `project_business_industry` | 1-15. Industry (DON'T CHANGE) [A] [IMPORTANT] | Customer | enum
- `project_business_language_primary` | 1-16. Language - Primary [B] | Customer | enum
- `project_business_language_restricted_list` | 1-17. Language - Restricted Languages [B] | Customer | json
- `project_attributes_known_employees` | 1-18. Known Employees [A] | Customer | string

## 1. Business - Advanced

Full descriptions: [1-business-advanced.md](1-business-advanced.md)

- `project_business_locations` | Business Locations [C] [IMPORTANT] | Customer | string
- `project_business_top_location_count` | Number of Business Locations [A] | Customer | number
- `project_business_top_name` | Parent Company Name [A] | Customer | string
- `project_business_top_url` | Parent Company Name Website [A] | Customer | string
- `project_business_type` | Business Type [A] | Customer | string
- `project_attributes_setting_hipaa_mode_enabled` | HIPAA Mode [A] | Customer | bool
- `project_attributes_static_additional_business_context` | Business Context - Additional [B] | Customer | string

## 2. Agent

Full descriptions: [2-agent.md](2-agent.md)

- `project_representative_agent_name` | 2-01. Agent Name [A] | Customer | string
- `project_representative_agent_title` | 2-02. Agent Title [A] | Customer | string
- `project_representative_agent_primary_language` | 2-03-A. Agent Primary Language [A] | Customer | enum
- `project_representative_agent_secondary_languages` | 2-03-B. Agent Secondary Languages [A] | Customer | json
- `project_representative_agent_multilingual` | 2-03-C. Agent Multilingual [A] | Customer | bool
- `project_representative_agent_voice_speaking_style` | 2-04-A. Agent Tone of Voice / Speaking Style for Voice Channels [A] | Customer | string
- `project_representative_agent_chat_speaking_style` | 2-04-B. Agent Tone of Voice for Chat Channels [A] | Customer | string
- `project_representative_agent_chat_formatting_style` | 2-04-C. Agent Chat Formatting Style [A] | Customer | string
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_voice` | 2-05-A. Voice - Integration Service - Voice To Voice Provider - GenAI - Voice [A] | Customer | enum
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_openai_voice` | 2-05-B. Voice - Integration Service - Voice To Voice Provider - OpenAI - Voice [A] | Customer | enum
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_grok_voice` | 2-05-C. Voice - Integration Service - Voice To Voice Provider - Grok - Voice [A] | Customer | enum
- `project_representative_agent_voice_phone_number` | 2-06. Agent Phone Number (AI Phone) (DON'T CHANGE) [A] | Customer | number
- `project_representative_agent_voice_disclaimer_phrase` | 2-07-A. Voice - Disclaimer Phrase [A] | Customer | string
- `project_representative_agent_voice_greeting_phrase` | 2-07-B. Voice - Greeting Phrase - Inbound [A] [IMPORTANT] | Customer | string
- `project_representative_agent_voice_greeting_phrase_recent_returning` | 2-07-C. Voice - Greeting Phrase - Recent Returning Customer [A] | Customer | string
- `project_representative_agent_voice_greeting_phrase_recent_returning_after_transfer` | 2-07-D. Voice - Greeting Phrase - Recent Returning Customer After Call Transfer [A] | Customer | string
- `project_representative_agent_voice_greeting_phrase_later_returning` | 2-07-E. Voice - Greeting Phrase - Returning Customer [A] | Customer | string
- `project_representative_agent_voice_greeting_phrase_later_returning_after_transfer` | 2-07-F. Voice - Greeting Phrase - Later Returning Customer After Call Transfer [A] | Customer | string
- `project_representative_agent_chat_greeting_phrase` | 2-08. Chat - Greeting Phrase [A] | Customer | string
- `project_representative_agent_gender` | 2-09. Agent Gender [A] | Customer | enum
- `project_attributes_setting_voice_integration_service_bypass_phone_number` | 2-10. Bypass Phone Number [A] | Customer | string
- `project_representative_agent_voicemail_detection_behavior_instruction` | 2-11. Voice - Voicemail Detection Behavior Instruction [A] | Customer | string
- `project_representative_agent_providing_prices_explicit_constraint` | 2-12. Explicit Constraint - Providing Prices [A] | Customer | string

## 2. Agent - Advanced

Full descriptions: [2-agent-advanced.md](2-agent-advanced.md)

- `project_representative_agent_voice_phone_area_code` | Voice - AI Phone - Area Code Primary [C] | Customer | number
- `project_representative_agent_voice_phone_alpha2_code` | Voice - AI Phone - ISO 3166-1 Alpha-2 Code [C] | Customer | string
- `project_representative_agent_voice_phone_fallback_area_code` | Voice - AI Phone - Area Code Fallback [C] | Customer | number
- `project_representative_agent_voice_phone_country_code` | Voice - AI Phone - Country Code [C] | Customer | number
- `project_representative_agent_voice_stt_model_id` | Voice - 4 - STT Model ID [C] | Customer | string
- `project_representative_agent_voice_stt_provider_id` | Voice - 3 - STT Provider ID [C] | Customer | string
- `project_representative_agent_voice_transcriber_language` | Voice - 5 - STT Transcriber Language [C] | Customer | string
- `project_representative_agent_voice_tts_model_id` | Voice - 2 - TTS Model ID [C] | Customer | string
- `project_representative_agent_voice_tts_provider_id` | Voice - 1 - TTS Provider ID [C] | Customer | string
- `project_attributes_setting_voice_integration_service` | Voice - Integration Service [C] [IMPORTANT] | Customer | enum
- `project_attributes_setting_voice_integration_service_voice_mode` | Voice - Integration Service - Voice Mode [C] [IMPORTANT] | Customer | enum
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider` | Voice - Integration Service - Voice To Voice Provider [C] [IMPORTANT] | Customer | enum

## 3. Knowledge Base

Full descriptions: [3-knowledge-base.md](3-knowledge-base.md)

- `project_attributes_products_and_services` | 3-01. Products & Services [A] | Customer | string
- `project_attributes_products_and_services_not_offering` | 3-02. Unavailable Products & Services [A] | Customer | string
- `project_attributes_current_specials` | 3-03. Specials [A] | Customer | string
- `project_attributes_faq` | 3-04. FAQ [A] | Customer | string
- `project_attributes_terms_and_conditions` | 3-05. Additional Details and Rules [B] | Customer | string
- `project_attributes_rag_knowledge_base_append_text` | 3-06-A. RAG - Knowledge Base - Text [A] | Customer | string
- `project_attributes_rag_knowledge_base_append_text_log` | 3-06-B. RAG - Knowledge Base - Text - Log [A] | Customer | string
- `project_attributes_rag_knowledge_base_append_text_reset` | 3-06-C. RAG - Knowledge Base - Text - Reset [A] | Customer | bool
- `project_attributes_rag_knowledge_base_append_websites` | 3-06-D. RAG - Knowledge Base - Websites [A] | Customer | string
- `project_attributes_rag_knowledge_base_append_websites_log` | 3-06-E. RAG - Knowledge Base - Websites - Log [A] | Customer | string
- `project_attributes_rag_knowledge_base_append_websites_reset` | 3-06-F. RAG - Knowledge Base - Websites - Reset [A] | Customer | bool

## 3. Knowledge Base - Advanced

Full descriptions: [3-knowledge-base-advanced.md](3-knowledge-base-advanced.md)

- `project_business_average_prices` | Average Prices [A] | Customer | string
- `project_attributes_current_specials_url` | Specials - Link (URL) [B] | Customer | string
- `project_attributes_products_and_services_served_area` | Products & Services - Area Served [A] | Customer | string
- `project_attributes_products_and_services_served_zip_codes` | Products & Services - ZIP Codes Served [B] | Customer | json

## 4. Agent Behavior

Full descriptions: [4-agent-behavior.md](4-agent-behavior.md)

- `project_attributes_setting_calendar_event_integration` | 4-04. Appointment - Calendar Event Integration [A] [IMPORTANT] | Customer | enum
- `project_attributes_setting_email_send_information_enabled` | 4-05. Email to User During Session - Enabled [B] [IMPORTANT] | Customer | bool
- `project_attributes_setting_email_send_information_allowed_content` | 4-06. Email to User During Session - Allowed Content [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_email_send_information_allowed_content_items` | 4-07. Email to User During Session - Allowed Content Items [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_sms_send_information_enabled` | 4-08. SMS to User During Session - Enabled [B] [IMPORTANT] | Customer | bool
- `project_attributes_setting_sms_send_information_allowed_content` | 4-09. SMS to User During Session - Allowed Content [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_sms_send_information_allowed_content_items` | 4-10. SMS to User During Session - Allowed Content Items [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_sms_provider` | 4-10-A. SMS Provider [C] | Customer | enum
- `project_business_manager_email` | 4-11. Email to Manager - Email Address [A] [IMPORTANT] | Customer | string
- `project_attributes_setting_transfer_call_enabled` | 4-12. Transfer Call to Manager - Enabled [B] [IMPORTANT] | Customer | bool
- `project_business_non_working_hour_escalation_phone` | 4-13. Transfer Call to Manager - Phone # Non-Working Hours [A] [IMPORTANT] | Customer | string
- `project_business_working_hour_escalation_phone` | 4-14. Transfer Call to Manager - Phone # Working Hours [A] [IMPORTANT] | Customer | string
- `project_attributes_setting_transfer_call_criteria` | 4-15. Transfer Call to Manager - Call Criteria [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_transfer_call_phone_numbers` | 4-16. Transfer Call to Manager - Advanced Phone Number Selection & Rules [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_session_ended_sms_enabled` | 4-17. Promotional SMS - Enabled [B] | Customer | bool
- `project_attributes_setting_session_ended_sms_content` | 4-18. Promotional SMS Content [B] | Customer | string
- `project_attributes_setting_instant_callback_on_abort_enabled` | 4-19. Phone - Instant Callback on Abort [A] | Customer | bool
- `project_attributes_setting_phone_dialpad_output_enabled` | 4-19-A. Phone - Dialpad Output [B] | Customer | bool

## 4. Agent Behavior - Advanced

Full descriptions: [4-agent-behavior-advanced.md](4-agent-behavior-advanced.md)

- `project_attributes_scenario` | Scenario [C] | Customer | enum
- `project_attributes_setting_additional_global_conversation_instruction` | Conversation - Additional Global Conversation Instruction [C] | Customer | string
- `project_attributes_setting_additional_limitations_and_restrictions` | Conversation - Additional Limitations and Restrictions [B] | Customer | string
- `project_attributes_setting_blocked_phone_numbers` | Phone - Blocked Numbers [A] | Customer | json
- `project_attributes_setting_spam_limit` | Phone - Spam Limit [A] | Customer | number
- `project_attributes_setting_booking_cancellation_enabled` | Booking - Cancellation - Enabled [B] | Customer | bool
- `project_attributes_setting_booking_cancellation_type` | Booking - Cancellation - Type [C] | Customer | enum
- `project_attributes_setting_booking_cancellation_url` | Booking - Cancellation - URL [B] | Customer | string
- `project_attributes_setting_booking_check_availability_enabled` | Booking - Check Availability - Enabled [B] | Customer | bool
- `project_attributes_setting_booking_check_availability_processing_type` | Booking - Check Availability - Processing Type [C] | Customer | enum
- `project_attributes_setting_booking_check_availability_payload_schema_template` | Booking - Check Availability - Schema [C] | Customer | json
- `project_attributes_setting_booking_check_availability_request_headers` | Booking - Check Availability - Request Headers [C] | Customer | json
- `project_attributes_setting_booking_check_availability_request_http_method` | Booking - Check Availability - Request HTTP Method [C] | Customer | enum
- `project_attributes_setting_booking_check_availability_validation_schema_template` | Booking - Check Availability - Validation Schema [C] | Customer | json
- `project_attributes_setting_booking_check_availability_type` | Booking - Check Availability - Type [C] | Customer | enum
- `project_attributes_setting_booking_check_availability_url` | Booking - Check Availability - Link (URL) [B] | Customer | string
- `project_attributes_setting_booking_check_availability_window` | Booking - Check Availability - Window [C] | Customer | number
- `project_attributes_setting_booking_check_availability_working_hours_status` | Booking - Check Availability - Working Hours Validation - Enabled [C] | Customer | bool
- `project_attributes_setting_booking_email` | Booking - Email [C] | Customer | string
- `project_attributes_setting_booking_enabled` | Booking - Enabled [B] | Customer | bool
- `project_attributes_setting_booking_fallback_processing_type` | Booking - Fallback Processing Type [C] | Customer | enum
- `project_attributes_setting_booking_check_availability_max_days_in_advance` | Booking - Max Days in Advance [C] | Customer | number
- `project_attributes_setting_booking_phrase_template_on_booking_submitting` | Booking - Phrase Template on Submitting [B] | Customer | string
- `project_attributes_setting_booking_phrase_template_on_booking_success` | Booking - Phrase Template on Successful Booking [B] | Customer | string
- `project_attributes_setting_booking_payload_schema_template` | Booking - Create Booking - Schema [C] | Customer | json
- `project_attributes_setting_booking_request_headers` | Booking - Request Headers [C] | Customer | json
- `project_attributes_setting_booking_meta_fields_schema_template` | Booking - Meta Fields Schema [C] | Customer | json
- `project_attributes_setting_booking_success_notification_on_email_enabled` | Booking - Email Notification On Successful Booking [B] | Customer | bool
- `project_attributes_setting_booking_success_notification_on_sms_enabled` | Booking - SMS Notification On Successful Booking [B] | Customer | bool
- `project_attributes_setting_booking_type` | Booking - Type [C] | Customer | enum
- `project_attributes_setting_booking_url` | Booking - Link (URL) [B] | Customer | string
- `project_attributes_setting_calculation_context` | Calculation Context [B] | Customer | string
- `project_attributes_setting_calculation_rules` | Calculation Rules [B] | Customer | string
- `project_attributes_setting_calendar_injection_is_enabled` | Calendar Injection [C] | Customer | bool
- `project_attributes_setting_chat_split_messages` | Chat - Split Long Messages [C] | Customer | bool
- `project_attributes_setting_check_spam_or_voicemail` | Check Spam or Voicemail [C] | Customer | bool
- `project_attributes_setting_connect_with_the_manager_in_case_of_unhandled_issues` | Conversation - Escalate Unresolved Issues To The Manager [C] | Customer | bool
- `project_attributes_setting_conversation_session_timeout_finished_chat` | Conversation - Session Timeout on Finished Chat [C] [IMPORTANT] | Customer | number
- `project_attributes_setting_conversation_session_timeout_finished_voice` | Conversation - Session Timeout on Finished Voice [C] [IMPORTANT] | Customer | number
- `project_attributes_setting_conversation_session_timeout_unfinished_chat` | Conversation - Session Timeout on Unfinished Chat [C] [IMPORTANT] | Customer | number
- `project_attributes_setting_conversation_session_timeout_unfinished_voice` | Conversation - Session Timeout on Unfinished Voice [C] [IMPORTANT] | Customer | number
- `project_attributes_setting_conversation_sources_map` | Conversation - Sources Map [C] | Customer | json
- `project_attributes_setting_data_injection_is_enabled` | Data Injection [C] | Customer | bool
- `project_attributes_setting_data_injection_max_summary_tokens` | Data Injection - Max Summary Tokens [C] | Customer | number
- `project_attributes_setting_data_injection_needs_summary` | Data Injection - Needs Summary [C] | Customer | bool
- `project_attributes_setting_data_injection_update_period` | Data Injection - Update Period [C] | Customer | number
- `project_attributes_setting_define_conversation_is_during_working_hours_enabled` | Conversation - Define Working Hours Status [C] | Customer | bool
- `project_attributes_setting_outbound_tasks_working_hours_status` | Outbound Tasks - Working Hours Enforcement - Enabled [C] | Customer | bool
- `project_attributes_setting_caller_id_pool` | Voice/SMS - Caller ID Pool [C] | Customer | json
- `project_attributes_setting_email_sender_name` | Email - Sender Name [A] | Customer | string
- `project_attributes_setting_email_signature_template` | Email - Signature Template [B] | Customer | string
- `project_attributes_setting_evaluate_ongoing_conversation_quality` | Conversation - Evaluate Ongoing Conversation Quality [C] | Customer | bool
- `project_attributes_setting_follow_up_timer_chat_interval_base` | Conversation - Follow-Up Timer - Chat - Interval - Base [C] | Customer | number
- `project_attributes_setting_follow_up_timer_voice_interval_agent_speech_ended` | Conversation - Follow-Up Timer - Voice - Interval - Agent Speech Ended [C] | Customer | number
- `project_attributes_setting_follow_up_timer_voice_interval_agent_speech_started` | Conversation - Follow-Up Timer - Voice - Interval - Agent Speech Started [C] | Customer | number
- `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_inbound` | Conversation - Follow-Up Timer - Voice - Interval - Conversation Started - Inbound [C] | Customer | number
- `project_attributes_setting_follow_up_timer_voice_interval_conversation_started_outbound` | Conversation - Follow-Up Timer - Voice - Interval - Conversation Started - Outbound [C] | Customer | number
- `project_attributes_setting_follow_up_timer_voice_interval_user_speech_ended` | Conversation - Follow-Up Timer - Voice - Interval - User Speech Ended [C] | Customer | number
- `project_attributes_setting_follow_up_timer_voice_interval_user_speech_started` | Conversation - Follow-Up Timer - Voice - Interval - User Speech Started [C] | Customer | number
- `project_attributes_setting_initial_thoughts` | Conversation - Initial Thoughts [C] | Customer | string
- `project_attributes_setting_meeting_check_availability_working_hours_status` | Appointment - Google Calendar Meeting - Working Hours Validation - Enabled [B] | Customer | bool
- `project_attributes_setting_meeting_duration` | Appointment - Google Calendar Meeting - Duration [B] | Customer | number
- `project_attributes_setting_meeting_setup_phrase` | Appointment - Google Calendar Meeting - Setup Phrase [B] | Customer | string
- `project_attributes_settings_platform_tools` | Conversation - Tools [C] | Customer | json
- `project_attributes_setting_products_and_services_background_check_location_enabled` | Products & Services - Check Location In the Background [B] | Customer | bool
- `project_attributes_setting_products_and_services_background_check_availability_enabled` | Products & Services - Check Availability In the Background [B] | Customer | bool
- `project_attributes_setting_products_and_services_structured_representation_enabled` | Products & Services - Structured Representation [C] | Customer | bool
- `project_attributes_setting_test_mode` | Testing - Test Mode [C] [IMPORTANT] | Customer | bool
- `project_attributes_setting_test_mode_phone_numbers` | Testing - Test Mode Phone Numbers [C] [IMPORTANT] | Customer | json
- `project_attributes_setting_timezone_reasoning_enabled` | Conversation - Time Zone Reasoning - Enabled [C] | Customer | bool
- `project_attributes_setting_time_format` | Time Format [C] | Customer | enum
- `project_attributes_setting_transfer_call_confirmation_phrase` | Transfer Call to Manager - Confirmation Phrase [B] | Customer | string
- `project_attributes_setting_transfer_call_custom_statement` | Transfer Call to Manager - Custom Statement [B] | Customer | string
- `project_attributes_setting_transfer_call_destination_availability_check_enabled` | Transfer Call to Manager - Destination Availability Check [C] | Customer | bool
- `project_attributes_setting_transfer_call_destination_format` | Transfer Call to Manager - Phone Number Format [C] | Customer | enum
- `project_attributes_setting_custom_transfer_call_enabled` | Voice - Transfer Call - Custom Transfer Call Enabled [C] | Customer | bool
- `project_attributes_setting_number_of_past_interactions_to_observe` | Conversation - Number of Past Interactions to Observe [C] | Customer | number
- `project_attributes_setting_session_ended_on_conversation_ended_enabled` | Conversation - End Session on Conversation End [C] | Customer | bool
- `project_attributes_setting_session_ended_full_processing_enabled` | Conversation - Session Ended - Full Processing Enabled [C] [IMPORTANT] | Customer | bool
- `project_attributes_setting_session_ended_reset_persona_attributes` | Conversation - Session Ended - Reset Persona Attributes [C] | Customer | bool
- `project_attributes_setting_waiting_mode_fallback_instruction` | Conversation - Waiting Mode - Fallback Instruction [C] | Customer | string
- `project_attributes_setting_waiting_mode_timeout` | Conversation - Waiting Mode - Timeout [C] | Customer | number
- `project_attributes_setting_test_mode_phone_numbers_static` | Project - Testing - Test Mode Phone Numbers Static [C] [IMPORTANT] | Project | json

## 5. Reports

Full descriptions: [5-reports.md](5-reports.md)

- `project_attributes_setting_asr_average_lead_value` | 5-01. ASR - Average Lead Value [A] | Customer | number
- `project_attributes_setting_asr_conversion_ratio` | 5-02. ASR - Conversion Ratio [A] | Customer | number
- `project_attributes_setting_asr_redirection_type_working_hours` | 5-03. ASR - Redirection Type (Working Hours) [A] | Customer | enum
- `project_attributes_setting_session_ended_report_enabled` | 5-04. Reports - Session Ended Report - Enabled [B] [IMPORTANT] | Customer | bool
- `project_attributes_setting_session_ended_report_content` | 5-05. Reports - Session Ended Report - Content [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_session_ended_report_criteria_template` | 5-06. Reports - Session Ended Report - Criteria [B] [IMPORTANT] | Customer | string
- `project_attributes_setting_session_ended_report_include_transcript` | 5-07. Reports - Session Ended Report - Transcript [B] | Customer | bool
- `project_attributes_setting_session_ended_report_include_utm_tags` | 5-08. Reports - Session Ended Report - UTM Tags [B] | Customer | bool

## 5. Reports - Advanced

Full descriptions: [5-reports-advanced.md](5-reports-advanced.md)

- `project_attributes_private_custom_schema_inbound_call_report` | Reports - Phone Inbound - Custom Schema [C] | Customer | json
- `project_attributes_setting_asr_recognition` | ASR - Working Hours Recognition [A] | Customer | number
- `project_attributes_setting_conversation_summary_instruction` | Reports - Conversation Summary Guidelines [B] | Customer | string
- `project_attributes_setting_send_report_during_conversation` | Reports - Send Report During Conversation - Enabled [C] | Customer | bool
- `project_attributes_setting_session_ended_report_include_conversation_and_record_urls` | Reports - Session Ended Report - Records Links [A] | Customer | bool
- `project_attributes_setting_session_ended_report_type_email` | Reports - Session Ended Report - Type - Email [C] | Customer | enum
- `project_attributes_setting_session_ended_webhook_auth_header` | Reports - Webhook - Authentication Header [C] | Customer | string
- `project_attributes_setting_session_ended_webhook_schema` | Reports - Webhook - Schema [C] | Customer | json
- `project_attributes_setting_session_ended_webhook_url` | Reports - Webhook - Link (URL) [C] | Customer | string
- `project_attributes_info_client_session_logs_table_link` | Reports - Client Session Logs Table - Link (URL) [C] | Customer | string
- `project_attributes_private_technical_owners` | Reports - Technical Owners [B] [IMPORTANT] | Customer | string

## 6. Support

Full descriptions: [6-support.md](6-support.md)

- `project_attributes_private_sa_version` | 6-01. SuperAgent Version [B] | Customer | string
- `project_attributes_free_notes` | 6-02. Free Notes [A] | Customer | string
- `project_attributes_chat_link_demo` | 6-01. Chat - Demo Link (URL) [B] | Project | string

## 6. Support - Advanced

Full descriptions: [6-support-advanced.md](6-support-advanced.md)

- `project_attributes_setting_hitl_monitoring_enabled` | HITL - Monitoring [C] | Customer | bool
- `project_attributes_setting_magic_browser_alert_enabled` | HITL - Magic Browser Alerting [C] | Customer | bool
- `project_attributes_support_log_document_link` | Support Log Document Link (URL) [B] | Customer | string

## 7. Customer Account

Full descriptions: [7-customer-account.md](7-customer-account.md)

- `customer_email` | Customer Email [A] | Customer | string
- `customer_first_name` | Customer First Name [A] | Customer | string
- `customer_last_name` | Customer Last Name [A] | Customer | string
- `customer_phone` | Customer Phone Number [A] | Customer | string

## 8. System

Full descriptions: [8-system.md](8-system.md)

- `project_attributes_private_dynamic_ami_template` | AMI - Template [C] | Customer | string
- `project_attributes_private_dynamic_ami_compiled` | AMI - Compiled [C] | Customer | string
- `project_attributes_private_dynamic_caller_id_routing` | Dynamic - Caller ID Routing [C] | Customer | json
- `project_attributes_private_dynamic_itm_template` | ITM - Template [B] | Customer | string
- `project_attributes_private_dynamic_itm_compiled` | ITM - Compiled [C] | Customer | string
- `project_attributes_private_dynamic_last_prepared_itm_compiled` | ITM - Prepared Source [C] | Customer | string
- `project_attributes_private_dynamic_itm_non_working_hours_compiled` | ITM - Non Working Hours - Compiled [C] | Customer | string
- `project_attributes_private_dynamic_itm_working_hours_compiled` | ITM - Working Hours - Compiled [C] | Customer | string
- `project_attributes_setting_session_ended_report_additional_criteria` | Reports - Session Ended Report - Additional Criteria [C] | Customer | json
- `project_attributes_setting_session_ended_report_additional_schema` | Reports - Session Ended Report - Additional Schema [C] | Customer | json
- `project_attributes_setting_session_ended_report_criteria_complete_template` | Reports - Session Ended Report - Criteria - Complete Template [C] | Customer | string
- `project_attributes_setting_session_ended_report_criteria_compiled` | Reports - Session Ended Report - Criteria - Compiled [C] | Customer | string
- `project_attributes_setting_session_ended_report_event_map` | Reports - Session Ended Report - Event Map [C] | Customer | json
- `project_attributes_setting_shadow_metrics_enabled` | Assessment - Shadow Metrics - Enabled [C] | Customer | bool
- `project_attributes_private_dynamic_booking_check_availability_payload_schema_compiled` | Booking - Check Availability - Schema Compiled [C] | Customer | json
- `project_attributes_private_dynamic_booking_schema_compiled` | Dynamic - Booking Schema Compiled [C] | Customer | json
- `project_attributes_private_account_initialized_first_time` | Account - Initialized First Time [C] | Customer | bool
- `project_attributes_private_data_injection_is_timer_running` | Data Injection - Timer Is Running [C] | Customer | bool
- `project_attributes_private_data_injection_payload` | Data Injection - Payload [C] | Customer | json
- `project_attributes_private_data_injection_retrieved_data` | Data Injection - Retrieved Data [C] | Customer | string
- `project_attributes_private_dynamic_agent_persona` | Dynamic - Agent Persona [C] | Customer | string
- `project_attributes_private_dynamic_agent_title` | Dynamic - Agent Title [C] | Customer | string
- `project_attributes_private_dynamic_business_context` | Dynamic - Business Context [C] | Customer | string
- `project_attributes_private_dynamic_booking_schema_template` | Dynamic - Booking Schema Template [C] | Customer | json
- `project_attributes_private_dynamic_booking_check_availability_schema_template` | Dynamic - Booking Check Availability Schema Template [C] | Customer | json
- `project_attributes_private_dynamic_business_locations_indexes` | Dynamic (LLM or non-LLM-based) - Business Locations Indexes [C] | Customer | json
- `project_attributes_private_dynamic_business_locations_object` | Dynamic (LLM or non-LLM-based) - Business Locations Object [C] | Customer | json
- `project_attributes_private_dynamic_email_signature` | Dynamic - Email Signature (Compiled) [C] | Customer | string
- `project_attributes_private_dynamic_email_variables` | Dynamic - Email Variables [C] | Customer | string
- `project_attributes_private_dynamic_first_customer_call_events_must_be_sent` | Dynamic - First Customer Call Events Must Be Sent [C] | Customer | bool
- `project_attributes_private_dynamic_intents_list` | Dynamic - Intents List [C] | Customer | string
- `project_attributes_private_dynamic_latest_executed_migration` | Migrations - Latest Executed Migration [C] | Customer | string
- `project_attributes_private_dynamic_phone_variables` | Dynamic - Phone Variables [C] | Customer | string
- `project_attributes_private_dynamic_products_and_services` | Dynamic (LLM or non-LLM-based) - Products & Services [C] | Customer | string
- `project_attributes_private_dynamic_prompt_calendar` | Dynamic (LLM-based) - Prompt Calendar [C] | Customer | string
- `project_attributes_private_dynamic_prompt_calendar_created_at` | Dynamic - Prompt Calendar Creation Date [C] | Customer | string
- `project_attributes_private_dynamic_rag_knowledge_base_append_text_structured` | Dynamic (LLM-based) - RAG - Knowledge Base - Text - Structured [C] | Customer | string
- `project_attributes_private_dynamic_rag_knowledge_base_append_websites_text` | Dynamic (LLM-based) - RAG - Knowledge Base - Websites - Text [C] | Customer | string
- `project_attributes_private_dynamic_rag_knowledge_base_append_websites_text_structured` | Dynamic (LLM-based) - RAG - Knowledge Base - Websites - Text - Structured [C] | Customer | string
- `project_attributes_private_dynamic_schedule_non_working_days` | Dynamic (LLM-based) - Schedule - Non-Working Days [C] | Customer | string
- `project_attributes_private_dynamic_schedule_working_days` | Dynamic (LLM-based) - Schedule - Working Days [C] | Customer | string
- `project_attributes_private_dynamic_schedule_working_days_hours_exceptions` | Dynamic (LLM-based) - Schedule - Exceptions [C] | Customer | string
- `project_attributes_private_dynamic_schedule_working_hours` | Dynamic (LLM-based) - Schedule - Working Hours [C] | Customer | string
- `project_attributes_private_dynamic_schedule_compiled` | Dynamic - Schedule - Compiled [C] | Customer | json
- `project_attributes_private_dynamic_tech_variables` | Dynamic - Tech Variables [C] | Customer | string
- `project_attributes_private_dynamic_v2v_native_config` | Dynamic - Voice - Accepted Native Configuration [C] | Customer | json
- `project_attributes_private_dynamic_v2v_native_connector_snapshot` | Dynamic - Voice - Native Connector Restore Baseline [C] | Customer | json
- `project_attributes_private_dynamic_v2v_native_mentions_cache` | Dynamic - Voice - Canvas Mentions Cache [C] | Customer | json
- `project_attributes_private_dynamic_variables` | Dynamic - General Variables [C] | Customer | string
- `project_attributes_private_dynamic_voice_greeting_phrase` | Dynamic - Voice - Greeting Phrase [C] | Customer | string
- `project_attributes_private_dynamic_session_ended_report_content_json` | Dynamic (LLM-based) - Reports - Session Ended Report Content JSON [C] | Customer | json
- `project_attributes_private_feature_flag_multi_location` | Agent - Multi-Location Feature [C] [IMPORTANT] | Customer | bool
- `project_attributes_private_feature_flag_agent_language_instructions_v2` | Feature Flag - Agent Language Instructions V2 [C] | Customer | bool
- `project_attributes_private_feature_flag_current_conversation_language` | Feature Flag - Current Conversation Language [C] | Customer | bool
- `project_attributes_private_feature_flag_booking_use_new_availability_formatted_response_processor` | Feature Flag - Booking - Use New Availability Formatted Response Processor [C] | Customer | bool
- `project_attributes_private_feature_flag_thoughts_genai_native_tools` | Feature Flag - Thoughts - GenAI Native Tools [C] | Customer | bool
- `project_attributes_private_feature_flag_email_universal_template` | Feature Flag - Email - Universal SendGrid Template [C] | Customer | bool
- `project_attributes_private_feature_flag_thoughts_step_state_tracing` | Feature Flag - Thoughts - Step State Tracing [C] | Customer | bool
- `project_attributes_private_feature_flag_v2v_native_tools` | Feature Flag - Voice - Native Context and Intent Tools [C] | Customer | bool
- `project_attributes_private_feature_flag_v2v_prompt_mutation_optimization` | Feature Flag - V2V Prompt Mutation Optimization [C] | Customer | bool
- `project_attributes_private_feature_flag_rag_append_websites_use_native_web_search_tool` | Feature Flag - RAG Append - Use Web Search [C] | Customer | bool
- `project_attributes_private_dynamic_llm_generated_scenarios` | Dynamic - Workflow Builder - LLM-Generated Scenarios [C] | Customer | json
- `project_attributes_private_dynamic_workflow_builder_canvas` | Dynamic - Workflow Builder - Canvas [C] | Customer | json
- `project_attributes_private_dynamic_workflow_builder_canvas_backup` | Dynamic - Workflow Builder - Canvas Backup [C] | Customer | json
- `project_attributes_private_dynamic_workflow_builder_canvas_library` | Dynamic - Workflow Builder - Canvas Library [C] | Customer | json
- `project_attributes_private_dynamic_workflow_builder_canvas_library_custom` | Dynamic - Workflow Builder - Canvas Library - Custom [C] | Customer | json
- `project_attributes_setting_external_reply_type` | Conversation - External Reply Type Handling [C] | Customer | enum
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions` | Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) [C] | Customer | json
- `project_attributes_private_dynamic_voice_integration_service_voice_to_voice_provider_genai_functions` | Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Runtime | Customer | json
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_description` | Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) | Customer | string
- `project_attributes_private_dynamic_voice_integration_service_voice_to_voice_provider_genai_functions_description` | Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Runtime | Customer | string
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_functions_enabled` | Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Enabled | Customer | bool
- `project_attributes_private_dynamic_voice_integration_service_voice_to_voice_provider_genai_functions_enabled` | Voice - Integration Service - Voice To Voice Provider - GenAI - Functions (Tools) Runtime | Customer | bool
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_context_type` | Voice - Integration Service - Voice To Voice Provider - GenAI - Set Turn Message Context | Customer | enum
- `project_attributes_setting_voice_integration_service_voice_to_voice_provider_genai_set_turn_message_type` | Voice - Integration Service - Voice To Voice Provider - GenAI - Set Turn Message Type [C] | Customer | enum
- `project_attributes_setting_init_attributes_metadata_enabled` | Project - Init - Setting-Up Attributes Metadata - Enabled [C] | Project | bool
- `project_attributes_setting_init_on_auto_update_enabled` | Project - Init - Initialization Process On Auto-Update - Enabled [C] | Project | bool
- `project_attributes_setting_rag_append_website_search_request_url` | Project - RAG Append - Website Search Request URL [C] | Project | string
- `project_attributes_setting_vibe_knowledge_base_search_url` | Project - Vibe Agent - Knowledge Base Search URL [C] | Project | string
- `project_attributes_setting_vibe_loop_max_depth` | Project - Vibe Agent - Loop Max Depth [C] | Project | number
- `project_attributes_setting_vibe_main_reasoning_effort` | Project - Vibe Agent - Main Reasoning Effort [C] | Project | enum
- `project_attributes_setting_vibe_project_init_timeout_seconds` | Project - Vibe Agent - Project Initialization Timeout [C] | Project | number
