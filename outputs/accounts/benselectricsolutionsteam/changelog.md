

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


