

# Changelog (v1 -> v2)

### Emergency Routing Rules

**Old (v1):**
```
For emergencies related to GNM Pressure Washing's managed gas stations after hours, calls will be patched directly to Ben. Caller identity and context (e.g., Shelley from GNM, or specific gas station details) will be used to identify these calls for direct transfer.
```

**New (v2):**
```
For emergencies related to GNM Pressure Washing's managed Chevron and Esso gas stations after hours, calls will be patched directly to Ben. Caller identity and context (e.g., Shelley from GNM, or specific gas station details) will be used to identify these calls for direct transfer. Shelley generally messages or texts details to Ben.
```

### Call Transfer Rules

**Old (v1):**
```
Initially, calls will forward from Ben's main line to Clara if Ben does not answer or declines. Once Ben's second personal phone number is active, Clara will be the primary contact. If a caller requests to speak with Ben (or a live person), Clara will obtain the purpose of the call and then transfer the call to Ben's second number. Clara will mention service call pricing ($150 for the first half-hour, then $49 per subsequent half-hour) only if specifically asked by the caller.
```

**New (v2):**
```
Initially, calls will forward from Ben's main line to Clara if Ben does not answer or declines (this conditional forwarding is enabled for Android devices). Once Ben's second personal phone number is active, Clara will be the primary contact. If a caller requests to speak with Ben (or a live person), Clara will obtain the purpose of the call and then transfer the call to Ben's second number. Clara will mention service call pricing ($150 for the first half-hour, then $49 per subsequent half-hour) only if specifically asked by the caller.
```

### After Hours Flow Summary

**Old (v1):**
```
For GNM Pressure Washing, emergency calls related to their managed gas stations will be patched directly to Ben. For all other callers, Clara will state that the company will get back to them on the next business day.
```

**New (v2):**
```
For GNM Pressure Washing, emergency calls related to their managed gas stations (Chevron, Esso) will be patched directly to Ben. For all other callers, Clara will state that the company will get back to them on the next business day.
```

### Questions Or Unknowns

**Old (v1):**
```
['Timezone for business hours.', 'Physical office address.', "Confirmation of services supported by Ben's Electric Solutions Team (e.g., purely electrical services, or other services mentioned for GNM Pressure Washing as well?).", "Specific definition of an emergency for Ben's Electric Solutions Team (beyond the GNM client).", "Ben's second phone number for call transfers.", 'Details for GNM Pressure Washing for identifying emergency calls (customer name, property name, address, primary contact, email, and phone number are needed for their specific properties/contacts).', 'Clarification on service call fee calculation: Ben stated $150 for the first half-hour, but calculation based on call-out fee ($115) and hourly rate ($98/hour, so $49/half-hour) suggests $164. Confirm which value to use.']
```

**New (v2):**
```
['Timezone for business hours.', 'Physical office address.', "Confirmation of services supported by Ben's Electric Solutions Team (e.g., purely electrical services, or other services mentioned for GNM Pressure Washing as well?).", "Specific definition of an emergency for Ben's Electric Solutions Team (beyond the GNM client).", "Ben's second phone number for call transfers.", 'Specific property details for GNM Pressure Washing (customer name, property names, addresses, primary contact details including email and phone number for Shelley) are needed to identify emergency calls for their specific properties/contacts.']
```




# Changelog (v1 -> v2)

### Emergency Definition

**Old (v1):**
```
['Any call designated as an emergency by specified existing clients (e.g., GNM Pressure Washing for 24/7 gas stations) during after-hours.']
```

**New (v2):**
```
['Any call designated as an emergency by GNM Pressure Washing, a property manager for Chevron and Esso gas stations operating 24/7, during after-hours.']
```

### Emergency Routing Rules

**Old (v1):**
```
For specific existing clients (e.g., GNM Pressure Washing), emergency calls after hours will be patched directly to Ben's second phone number. For all other callers during after-hours, they will receive a callback on the next business day.
```

**New (v2):**
```
For the specific existing client GNM Pressure Washing, emergency calls after hours will be patched directly to Ben's second phone number. The caller (Shelly from GNM) will provide gas station-specific details. For all other callers during after-hours, they will be informed that they will receive a callback on the next business day.
```

### Call Transfer Rules

**Old (v1):**
```
During office hours: If a caller wishes to speak to Ben, Clara can transfer the call to Ben's second phone number after getting a brief purpose of the call. No explicit mention of timeouts or retries. The second number is expected to be active by Friday.
```

**New (v2):**
```
During initial setup, if Ben does not answer or declines an incoming call on his main line, it will be forwarded to Clara. Once Ben's second personal phone number is active (expected by Friday), Clara will be the first point of contact for all incoming calls on the main business line. If a caller wishes to speak to Ben, Clara will obtain a brief purpose of the call and then transfer it to Ben's second personal phone number. There is no explicit mention of timeouts or retries if a transfer fails, or what to say if it fails.
```

### After Hours Flow Summary

**Old (v1):**
```
For specific existing clients (e.g., GNM Pressure Washing for 24/7 gas stations) reporting an emergency, the call will be patched directly to Ben's second phone number after getting the call context. For all other callers, they will be informed that they will receive a callback on the next business day.
```

**New (v2):**
```
For specific existing clients, GNM Pressure Washing, who manage 24/7 Chevron and Esso gas stations and report an emergency, the call will be patched directly to Ben's second phone number after getting the call context (gas station details). For all other callers, they will be informed that they will receive a callback on the next business day.
```

### Office Hours Flow Summary

**Old (v1):**
```
Incoming calls will be initially handled by Clara. If a caller asks, Clara will mention the $115 service call fee for a site visit. If a caller wishes to speak to Ben, Clara will transfer the call to Ben's second phone number after getting a brief purpose of the call. Ben's main phone line will forward incoming calls to Clara, while outbound calls and text messages on Ben's main line will function normally.
```

**New (v2):**
```
Incoming calls will be initially handled by Clara. Call forwarding to Clara will occur if Ben does not answer or declines the call on his main line. Once Ben's second personal phone number is active, Clara will be the first point of contact for all incoming calls. If a caller asks, Clara will mention the $115 service call fee for a site visit. If a caller wishes to speak to Ben, Clara will transfer the call to Ben's second phone number after obtaining a brief purpose of the call. Ben's main phone line will forward incoming calls to Clara (either if he doesn't answer/declines or always, once the second number is active), while outbound calls and text messages on Ben's main line will function normally.
```

### Questions Or Unknowns

**Old (v1):**
```
['What is the full address of the office?', 'What is the specific timezone for the business hours (8 AM - 4:30 PM)?', "What are the exact criteria or triggers that constitute an 'emergency' for the specified existing clients (e.g., GNM Pressure Washing)?", "What specific electrical services are offered by Ben's Electric Solutions Team?", 'What is the fallback procedure if a call transfer to Ben fails (e.g., voicemail, retry, message to caller)?', 'Will there be a specific message played to non-emergency callers after hours before informing them about the next business day callback?', "What is Ben's second phone number that Clara will transfer calls to?"]
```

**New (v2):**
```
['What is the full address of the office?', 'What is the specific timezone for the business hours (8 AM - 4:30 PM)?', "What specific electrical services are offered by Ben's Electric Solutions Team?", 'What is the fallback procedure if a call transfer to Ben fails (e.g., voicemail, retry, message to caller)?', 'Will there be a specific message played to non-emergency callers after hours before informing them about the next business day callback?', "What is Ben's main phone number for SMS notifications?", "What are the full contact details for GNM Pressure Washing, including Shelly's full name and specific emergency details if any?"]
```

### Notes

**Old (v1):**
```
Ben is currently handling all incoming calls personally, except for direct calls to team members from steady contractors. Ben will provide a second phone number for personal use, which will be used for call transfers from Clara. This second number is expected to be active by Friday. Initial setup will involve forwarding main line calls to Clara only if Ben doesn't answer or declines. Once the second number is ready, Clara will be the first point of contact. Notifications for new calls (email and SMS) will be sent to info@benselectricsolutionsteam.com and Ben's main phone number, respectively. The service call fee is $115 for a call-out, plus $98/hour (in half-hour increments) for residential work. This will only be mentioned by Clara if explicitly asked by the caller. The system will be calibrated in the initial days to minimize unwanted transfers (e.g., spam/sales calls).
```

**New (v2):**
```
Ben is currently handling all incoming calls personally, except for direct calls to team members from steady contractors. Ben has a second phone number that will be used for Clara to transfer calls to, and it is expected to be active by Friday. Initial setup will involve forwarding main line calls to Clara only if Ben doesn't answer or declines. Once the second number is ready, Clara will be the first point of contact. Notifications for new calls (email and SMS) will be sent to info@benselectricsolutionsteam.com and Ben's main phone number, respectively. The service call fee is $115 for a call-out, plus $98/hour (in half-hour increments) for residential work. Clara will only mention this if explicitly asked by the caller. The system will be calibrated in the initial days to minimize unwanted transfers (e.g., spam/sales calls). A follow-up meeting is scheduled for Friday at 2:00 PM to review test calls and make any necessary adjustments.
```


