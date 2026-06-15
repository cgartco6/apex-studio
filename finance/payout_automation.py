[Insert Strict System-Level Engineering Prompt]

Generate the complete source code for `finance/payout_automation.py`.
This module handles secure, programmatic outbound balance clearings and multi-party vendor split-payouts.

Requirements:
1. PAYOUT TRANSACTION ROUTER: Build a processing script that calculates merchant splits minus platform operational fees.
2. BANKING API INTEGRATION: Implement settlement endpoints structured for local EFT clearing layers (such as Ozow payouts or South African clearing bank host-to-host file formats) and global payout systems.
3. IDEMPOTENCY SAFETY: Force unique tracking token checks on every payout instruction. If an instruction is triggered twice, the system must block duplicate fund movements instantly to protect liquidity.
