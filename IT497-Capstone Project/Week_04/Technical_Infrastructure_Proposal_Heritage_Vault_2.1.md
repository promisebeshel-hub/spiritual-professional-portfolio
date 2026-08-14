<div style="margin-bottom: 20px;">
  <a href="javascript:history.back()" style="text-decoration: none; font-weight: bold; background: #21262d; color: #58a6ff; padding: 8px 14px; border-radius: 6px; border: 1px solid #30363d; display: inline-block; cursor: pointer;">⬅️ Back to Previous Page</a>
</div>

Prepared for: FamilySearch
Prepared by: Promise Beshel, Systems Engineering Division
Course: ENSIGN COLLEGE | IT370 / IT497
Date: July 2026

# Technical Infrastructure Proposal: Heritage Vault 2.1

## Executive Summary
FamilySearch is modernizing its core record-preservation infrastructure by expanding the Heritage Vault platform to Version 2.1. This enterprise proposal upgrades the baseline Linux infrastructure (v2.0) into a Zero Trust, AI-governed, highly resilient digital repository. Because FamilySearch preserves billions of global genealogical records and sacred LDS ordinance data, Heritage Vault 2.1 establishes an advanced architectural blueprint balancing sub-millisecond query performance with Zero Trust security, Privacy-by-Design governance, WCAG 2.2 accessibility, and sustainable cloud operations.

---

## 1. Zero Trust Security Architecture
Building upon the SELinux Enforcing modes, firewalld default-drop rules, and LUKS storage encryption from Heritage Vault 2.0, Version 2.1 transitions the platform from a perimeter-based security model to a strict **Zero Trust Architecture (ZTA)**:

* **Continuous Identity Verification:** Replaces static session tokens with continuous risk-based authentication via OAuth 2.0 / OIDC and mutual TLS (mTLS) for all inter-service microcommunication.
* **Device Posture Validation:** Enforces Endpoint Detection and Response (EDR) agent verification before granting administrative or API-level access to internal node clusters.
* **Just-in-Time (JIT) Administrative Privileges:** Replaces static `/etc/sudoers` access with short-lived, time-bound JIT administrative roles granted via PAM integration, requiring explicit multi-party approval for production system changes.
* **Network Micro-segmentation:** Utilizes Cilium/eBPF network policies inside Kubernetes clusters to isolate database pods, application containers, and edge proxies, ensuring that compromise of an application container cannot lead to lateral movement into primary database stores.

---

## 2. Ethical AI Governance & Record Integrity
FamilySearch increasingly leverages Artificial Intelligence and Machine Learning for Optical Character Recognition (OCR), automated record matching, duplicate identification, and search indexing. Heritage Vault 2.1 introduces a formal Ethical AI Governance framework:

* **Human-in-the-Loop (HITL) Review:** Machine learning models are strictly prohibited from executing automated, permanent merges of ancestral family trees or ordinance records. Any AI record-matching confidence score below 98% requires mandatory review by a human genealogist or patron.
* **Explainable AI (XAI) & Confidence Scoring:** Every AI-generated record match displays an explicit confidence score and an audit breakdown detailing *why* the link was suggested (e.g., matching census dates, spatial proximity, or phonetic surname algorithms).
* **Cross-Cultural Bias Testing:** AI indexing models undergo routine auditing against non-Western naming conventions, patronymic systems, and varied historical document structures to prevent algorithmic drop-off in global record representation.
* **Manual Correction & Rollback Workflows:** Provides immutable version history allowing patrons to challenge, correct, or revert inaccurate AI-generated index suggestions instantly.

---

## 3. Privacy-by-Design & Regulatory Compliance
Moving beyond baseline GDPR and CCPA legal compliance, Heritage Vault 2.1 embeds Privacy-by-Design directly into system architecture:

* **Data Minimization:** API endpoints and ingestion pipelines harvest strictly necessary metadata fields, dropping non-essential client browser footprints and tracking telemetry at the edge proxy tier.
* **Automated Right-to-Delete Pipelines:** Implements automated asynchronous worker queues that process patron deletion requests across active databases, caches, and offsite index mirrors within mandated 30-day SLA windows.
* **Granular User Consent Management:** Patrons control exact sharing boundaries for living family records through cryptographic access control keys stored within private user vaults.
* **Automated Data Retention & Anonymization Schedules:** Historical records containing PII of living individuals are dynamically obfuscated until verified public-domain or age-threshold conditions are met.

---

## 4. Accessibility & Inclusive Design (WCAG 2.2)
To ensure sacred genealogical resources remain available to all users worldwide regardless of physical ability, Heritage Vault 2.1 mandates full compliance with **Web Content Accessibility Guidelines (WCAG) 2.2 Level AA**:

* **Screen Reader & Keyboard Navigation:** Complete ARIA-labeling across historical tree viewers and tabular search interfaces, enabling 100% keyboard-only navigation.
* **Visual Adaptability:** High-contrast color palettes, adjustable font scalers, and dynamic text reflow supporting 200% zoom without horizontal scrolling.
* **Instructional Media Accessibility:** Closed captioning, multi-language transcripts, and descriptive audio tracks for all embedded video demonstrations and platform training assets.

---

## 5. Sustainable Cloud Infrastructure
Modern global infrastructure must minimize its operational carbon footprint and computational waste:

* **Predictive Kubernetes Auto-scaling:** Leverages Horizontal Pod Autoscalers (HPA) driven by AI load forecasting models to spin down dormant application pods during regional low-usage hours, reducing idle energy consumption by up to 35%.
* **Power-Aware Carbon Scheduling:** Non-time-sensitive batch processing workloads (such as deep OCR text extraction and bulk image compression) are scheduled to execute in AWS/cloud regions during periods of peak renewable energy availability.
* **Cold Storage Tiering:** Historical image files older than 5 years without active read queries are automatically migrated from high-power NVMe storage to cold, energy-efficient object storage tiers.

---

## 6. Immutable Disaster Recovery & High Availability
To guarantee absolute protection against physical catastrophic events and modern ransomware threats, Heritage Vault 2.1 expands disaster recovery targets:

* **Immutable Ransomware-Resistant Storage:** Offsite backups are written to Object Lock storage tiers configured in Write-Once-Read-Many (WORM) mode, preventing alteration or encryption even if root administrative credentials are compromised.
* **Automated Multi-Region Failover:** HAProxy and AWS Route 53 health-check agents trigger automated DNS failover to secondary cloud regions if primary datacenter response latency exceeds 500ms over a 30-second window.
* **Aggressive Recovery Objectives:**
  * **Recovery Time Objective (RTO):** $< 30$ minutes for total system restoration.
  * **Recovery Point Objective (RPO):** $< 5$ minutes for zero transactional data loss.

---

## 7. Full-Stack Observability & AI Anomaly Detection
Replaces basic system monitoring with comprehensive enterprise telemetry:

* **Observability Stack:** Deploys Prometheus for metric scraping, Grafana for real-time visualization dashboards, the ELK Stack (Elasticsearch, Logstash, Kibana) for centralized log management, and OpenTelemetry for distributed trace analysis across microservices.
* **AI-Assisted Threat Detection:** Integrates SIEM log analyzers equipped with unsupervised machine learning to detect anomalous user behavior (such as mass record exfiltration attempts or unusual credential usage) in real-time, automatically revoking compromised session tokens.

---

## Summary Comparison: Heritage Vault 2.0 vs. Heritage Vault 2.1

| Operational Domain | Heritage Vault 2.0 Baseline | Heritage Vault 2.1 Refinement |
| :--- | :--- | :--- |
| **Authentication** | SSH Keys, MFA, static RBAC | Zero Trust, mTLS, Just-In-Time (JIT) privileges |
| **Data Protection** | LUKS Encryption, SELinux, Firewalld | Privacy-by-Design, Automated Right-to-Delete |
| **AI Systems** | Basic OCR & Record Indexing | Human-in-the-Loop review, Explainable AI, Bias Audits |
| **Disaster Recovery** | ZFS Snapshots, Offsite Backups | Immutable WORM Backups, Automated Multi-Region Failover |
| **Accessibility** | Basic Web UI | WCAG 2.2 AA Compliance, Screen-Reader Native |
| **Sustainability** | Static Resource Allocation | Predictive Auto-scaling, Carbon-Aware Job Scheduling |
| **Observability** | Local Linux Logs & Sysctl Tuning | Prometheus, Grafana, OpenTelemetry, AI Anomaly Detection |
