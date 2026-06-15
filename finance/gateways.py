[Insert Strict System-Level Engineering Prompt]

Generate the full code for `finance/gateways.py` to handle all incoming platform checkouts.

Requirements:
1. LOCAL GATEWAY MATRIX: Complete implementation for PayFast and Ozow API wrappers. Generate explicit cryptographic signatures for parameters, handle instant EFT notification (ITN) verification webhooks, and process raw ZAR transactions securely.
2. GLOBAL CARD GATEWAY: Integrate a robust Stripe PaymentIntent wrapper handling foreign currencies, processing global card inputs, and passing verified payment tokens smoothly back to the core.
3. FAILOVER LOGIC: Build an automatic fallback loop ensuring that if a specific processing gateway reports down-time, the customer session is securely rerouted to alternative checkouts without losing state.
