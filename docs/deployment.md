# Deployment

The development server is not a clinical deployment blueprint. Put Streamlit
behind TLS and authentication; isolate storage; configure upload limits; scan
files; de-identify exports; audit access; pin dependencies; and run security,
performance, and clinical validation.

Future reference deployments will include Docker, Kubernetes health checks,
object storage, background inference, REST/FHIR/DICOMweb services, and secrets
management.

