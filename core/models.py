from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class AccountMemo(BaseModel):
    account_id: str = Field(description="Unique identifier for the account (e.g., lowercase company name without spaces)")
    company_name: str = Field(description="Full name of the company")
    business_hours: str = Field(description="Business hours (days, start, end, timezone)")
    office_address: Optional[str] = Field(None, description="Physical office address if present")
    services_supported: List[str] = Field(default_factory=list, description="List of services supported by the company")
    emergency_definition: List[str] = Field(default_factory=list, description="List of triggers or conditions that qualify as an emergency")
    emergency_routing_rules: str = Field(description="Rules for routing emergencies (who to call, order, fallback)")
    non_emergency_routing_rules: str = Field(description="Rules for handling non-emergencies")
    call_transfer_rules: str = Field(description="Transfer rules (timeouts, retries, what to say if fails)")
    integration_constraints: str = Field(description="System integration constraints like 'never create sprinkler jobs in ServiceTrade'")
    after_hours_flow_summary: str = Field(description="Summary of the after hours flow")
    office_hours_flow_summary: str = Field(description="Summary of the office hours flow")
    questions_or_unknowns: List[str] = Field(default_factory=list, description="List of missing details or unknowns needing clarification")
    notes: str = Field(description="Short additional notes")

class RetellAgentSpec(BaseModel):
    agent_name: str
    voice_style: str = Field(default="professional, empathetic, clear")
    system_prompt: str
    key_variables: Dict[str, str] = Field(default_factory=dict)
    tool_invocation_placeholders: List[str] = Field(default_factory=list, description="DO NOT MENTION TO CALLER")
    call_transfer_protocol: str
    fallback_protocol: str
    version: str = Field(default="v1")
