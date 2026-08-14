<div style="margin-bottom: 20px;">
  <a href="javascript:history.back()" style="text-decoration: none; font-weight: bold; background: #21262d; color: #58a6ff; padding: 8px 14px; border-radius: 6px; border: 1px solid #30363d; display: inline-block; cursor: pointer;">⬅️ Back to Previous Page</a>
</div>

# Technical Projects & Coursework Showcase

---

## Overview

This section highlights hands-on technology projects completed throughout my degree, demonstrating core competencies in cloud architecture, infrastructure as code (IaC), cybersecurity scripting, database administration, and automated network engineering.

---

## 1. Cloud Administration & Azure Technologies (IT330 / AZ-104)

Designed, deployed, and secured cloud infrastructure solutions across **Microsoft Azure**, validating competency across the entire **AZ-104: Microsoft Azure Administrator** syllabus.

* **AZ-104 Practice Exam Portfolio Performance:**
  * **Practice Exam 1:** Overall **80%** (Identities & Governance: 93%, Resource Monitoring: 90%)
  * **Practice Exam 2:** Overall **80%** (Storage Management: 100%, Compute Resources: 85%)
  * **Practice Exam 3:** Overall **85%** (Virtual Networking: 92%, Resource Monitoring: 89%)
  * **Practice Exam 4:** Overall **85%** (Storage Management: 91%, Identities & Governance: 87%)
* **Key Deliverables:** Configured Entra ID RBAC roles, Azure Policy initiatives, VNet peering with gateway transit, Azure Storage replication/encryption, and VM scale sets.
* **Demonstration Video:**

<details>
  <summary>🎬 <strong>Play IT330 Azure Technologies Lab Demonstration</strong></summary>
  <br>
  <iframe src="https://player.vimeo.com/video/1217763802" width="100%" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="max-width: 640px; border-radius: 5px; border: 1px solid #ccc;"></iframe>
</details>

---

## 2. Scripting for Security Operations & C2 Architectures (IT316)

Authored a comprehensive 22-page technical analysis paper and engineered custom Python socket scripts simulating **Command and Control (C2)** client-server operations and security automation.

* **Key Deliverables:**
  * Developed multi-threaded socket listeners (`custom_netcat_svr.py`) and asynchronous background client agents (`custom_netcat_cli-1.py`) with non-blocking `stdin`/`stdout`/`stderr` stream piping.
  * Implemented Base64-encoded chunked file transfer functions (`upload` & `download`) with exception handling and SHA-256 hash checks.
  * Evaluated offensive adversary techniques (DNS tunneling, domain fronting, asynchronous beaconing with sleep jitter) and defensive threat-hunting strategies (Sysmon logs, YARA rules, Snort signatures).
* **Core Competencies:** Socket Networking, Multi-threading, Process Piping, Threat Intelligence (MITRE ATT&CK Mapping), Offensive/Defensive Scripting.

---

## 3. Infrastructure as Code (IaC) & Proxmox Virtualization (IT316 Lab)

Provisioned and automated virtualized Linux environments by integrating **Terraform** with a **Proxmox Virtual Environment (PVE 9.1.5)** hypervisor cluster.

* **Key Deliverables:**
  * Configured Kali Linux management nodes (`pbeshel-Kali-VM`) to interface with Proxmox cluster nodes (`22417-GEN8`).
  * Wrote HCL infrastructure configurations using the `bpg/proxmox` provider to automate VM cloning, CPU/RAM allocation, and disk provisioning.
  * Executed automated state workflows (`terraform init`, `terraform validate`, `terraform plan`, and `terraform apply`) to deploy headless Ubuntu server instances (`pbeshel-ubuntu-vm`) in under 15 seconds.
* **Core Competencies:** Infrastructure as Code (IaC), HashiCorp Terraform, Proxmox VE, Virtual Machine Provisioning, SSH Automation.

---

## 4. Relational Database Development & Advanced Querying (IT143)

Designed and implemented relational database systems using **Microsoft SQL Server 2022**. Focused on schema normalization, complex T-SQL queries, joins, and data integrity.

* **Key Deliverables:** SQL scripts (`.sql`), relational architecture diagrams, and data analysis presentations.
* **Core Competencies:** Schema design, primary/foreign key constraints, views, stored procedures, and query optimization.
* **Demonstration Videos:**

<details>
  <summary>🎬 <strong>Play IT143 Lab Demonstration 1</strong></summary>
  <br>
  <iframe src="https://player.vimeo.com/video/1209346092" width="100%" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="max-width: 640px; border-radius: 5px; border: 1px solid #ccc;"></iframe>
</details>

<br>

<details>
  <summary>🎬 <strong>Play IT143 Lab Demonstration 2</strong></summary>
  <br>
  <iframe src="https://player.vimeo.com/video/1211081451" width="100%" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="max-width: 640px; border-radius: 5px; border: 1px solid #ccc;"></iframe>
</details>

---

## 5. Automated Database Provisioning Engine (CS104)

Developed an automated database pipeline using **Python** and **SQLite** to programmatically generate database structures, ingest structured JSON configurations, and present data.

* **Repository Architecture:** `createDB.py`, `insert_recs.py`, `show_records.py`, `people.db`.
* **Demonstration Videos:**

<details>
  <summary>🎬 <strong>Play CS104 Python/SQLite Pipeline Demo 1</strong></summary>
  <br>
  <iframe src="https://player.vimeo.com/video/1183551441?h=e3b38920ed" width="100%" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="max-width: 640px; border-radius: 5px; border: 1px solid #ccc;"></iframe>
</details>

---

## 6. Network Infrastructure & Cloud Architecture (IT160 / IT210 / IT370)

Designed, configured, and simulated localized and enterprise network environments using **Cisco Packet Tracer** and managed cloud resources on **Microsoft Azure**.

* **Key Deliverables:** Network topology configurations, subnetting designs, router/switch command-line setup, Access Control Lists (ACLs), Azure VM administration runbooks.
* **Demonstration Videos:**

<details>
  <summary>🎬 <strong>Play Network Infrastructure Lab Demo 1</strong></summary>
  <br>
  <iframe src="https://player.vimeo.com/video/1182783917?h=a885789a23" width="100%" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="max-width: 640px; border-radius: 5px; border: 1px solid #ccc;"></iframe>
</details>

---

<h2 id="it497-capstone">🎓 IT 497 — Capstone Project Deliverables & Weekly Progress</h2>

<!-- WEEK 1 -->
<details id="week-1" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 1: Foundation, Alignment & Personal Agency (Click to Expand)</strong></summary>

<br>

* **Step 1 — Task 1:** SMART goals & intro reflection video.
* **Step 2 — Task 2:** Guiding principles baseline (Integrity, Continuous Revelation, Servant Leadership).
* **Step 3 — Task 3:** Portfolio repository deployment.
</details>

<hr>

<!-- WEEK 2 -->
<details id="week-2" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 2: Deepening Engagement & Platform Governance (Click to Expand)</strong></summary>

<br>

* **Step 1 — Task 1:** Systems analysis and strategic goal refinement.
* **Step 2 — Task 2:** Ethical governance and data privacy analysis.
* **Step 3 — Task 3:** Technical documentation pipelines.
</details>

<hr>

<!-- WEEK 3 -->
<details id="week-3" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 3: Ethical Evaluation & Architectural Refinement (Click to Expand)</strong></summary>

<br>

* **Step 1 — Task 1:** Capital One root-cause breach analysis.
* **Step 2 — Task 2:** Scriptural integration for technical exactness.
* **Step 3 — Task 3:** Peer review preparation.
</details>

<hr>

<!-- WEEK 4 -->
<details id="week-4" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 4: Expansion, Deepening & Project Refinement (Click to Expand)</strong></summary>

<br>

* **Step 1 — Task 1:** Video reflection on personal agency.
* **Step 2 — Task 2:** Expanded spiritual principles alignment.
* **Step 3 — Task 3:** DevSecOps alternative to 2019 Capital One breach.
* **Step 4 — Task 4:** Heritage Vault 2.1 proposal and peer review.
</details>

<hr>

<!-- WEEK 5 -->
<details id="week-5" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 5: Integration, Reflection, and Design Enhancement (Click to Expand)</strong></summary>

<br>

* **Task 1:** Christlike attributes & warning signs matrix.
* **Task 2:** Usability testing report & Capital One ethical reflection.
* **Task 3:** Temple reflection & Disciple-Leader Systems Blueprint.
* 🔗 <a href="../IT497-Capstone%20Project/Week_05/integration_reflection_and_design.html" target="_blank"><strong>View Full Week 5 Report</strong></a>
</details>

<hr>

<!-- WEEK 6 -->
<details id="week-6" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 6: Finalization, Peer Reviews, and Presentations Report (Click to Expand)</strong></summary>

<br>

* **Task 1:** 36-month ongoing action plan & goal evolution essay.
* **Task 2:** Comprehensive peer reviews report (Eric & Mitchell reviews; Chinenye & McSylvester feedback matrix).
* **Task 3:** 6-slide final presentation transcript, slide download, and Vimeo presentation link.
* 🔗 <a href="../IT497-Capstone%20Project/Week_06/finalization_and_presentations.html" target="_blank"><strong>View Full Week 6 Capstone Report</strong></a>
</details>

<hr>

<!-- WEEK 7 -->
<details id="week-7" markdown="1">
<summary style="cursor: pointer;"><strong>🗓️ Week 7: Return & Report and Community Reflection (Click to Expand)</strong></summary>

<br>

* **Task 1:** Postcourse return & report evaluating initial goals against final milestones.
* **Task 2:** Handwritten future aspirations submission.
* **Task 3:** Group 7 Roundtable community discussion with peer Eze Eze Okoro.
* 🔗 <a href="../IT497-Capstone%20Project/Week_07/return_and_report.html" target="_blank"><strong>View Full Week 7 Return & Report Page</strong></a>
* 🔗 <a href="../IT497-Capstone%20Project/Week_07/roundtable_discussion.html" target="_blank"><strong>View Week 7 Roundtable Discussion Summary</strong></a>
</details>

---

## 🧭 Navigation

* ⬅️ [Back to Home](../index.html)
* 📄 [View Professional Resume](resume.html)
* ⚖️ [Proceed to Ethical Analysis](ethical-analysis.html)
* 🙏 [Spiritual Guiding Principles](../spiritual/guiding-principles.html)
