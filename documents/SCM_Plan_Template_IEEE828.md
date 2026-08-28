# Team 3 Track Overflow — Software Configuration Management Plan

*Prepared in conformance with IEEE Std 828™-2005*

## Document Information

| Field | Value |
|---|---|
| Document Version | [e.g., 1.0] |
| Date | [Month DD, YYYY] |
| Prepared By | [Name / Role] |
| Approved By | [Name / Role] |
| Course / Project | [Course number or program] |
| Status | [Draft / Baseline / Released] |

## Revision History

| Version | Date | Description of Change | Author |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## How to Use This Template

This template follows the six required classes of information and section sequence in Table 1 of IEEE Std 828-2005. Each subsection includes:

- A **Guidance** line summarizing what the standard requires — delete or keep for reference
- Bulleted minimum-content items where the standard specifies exact elements to record
- A `[bracketed placeholder]` where you enter your project's content

Before finalizing: replace every `[bracketed placeholder]`, complete the Revision History, and review the Appendix A checklist. If any required item does not apply to your project, keep the class heading but state the omission and reason in §1.2, per Clause 4.2 of the standard. Headings use standard Markdown levels (`##` = major class, `###` = subsection, `####` = sub-subsection), so the links below work in any renderer with heading anchors (GitHub, GitLab, VS Code preview, most wikis).

## Table of Contents

- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Scope](#12-scope)
  - [1.3 Definitions, Acronyms, and Abbreviations](#13-definitions-acronyms-and-abbreviations)
  - [1.4 References](#14-references)
- [2. SCM Management](#2-scm-management)
  - [2.1 Organization](#21-organization)
  - [2.2 SCM Responsibilities](#22-scm-responsibilities)
  - [2.3 Applicable Policies, Directives, and Procedures](#23-applicable-policies-directives-and-procedures)
  - [2.4 Management of the SCM Process](#24-management-of-the-scm-process)
- [3. SCM Activities](#3-scm-activities)
  - [3.1 Configuration Identification](#31-configuration-identification)
    - [3.1.1 Identifying Configuration Items](#311-identifying-configuration-items)
    - [3.1.2 Naming Configuration Items](#312-naming-configuration-items)
    - [3.1.3 Acquiring Configuration Items](#313-acquiring-configuration-items)
  - [3.2 Configuration Control](#32-configuration-control)
    - [3.2.1 Requesting Changes](#321-requesting-changes)
    - [3.2.2 Evaluating Changes](#322-evaluating-changes)
    - [3.2.3 Approving or Disapproving Changes](#323-approving-or-disapproving-changes)
    - [3.2.4 Implementing Changes](#324-implementing-changes)
  - [3.3 Configuration Status Accounting](#33-configuration-status-accounting)
  - [3.4 Configuration Evaluation and Reviews](#34-configuration-evaluation-and-reviews)
  - [3.5 Interface Control](#35-interface-control)
  - [3.6 Subcontractor/Vendor Control](#36-subcontractorvendor-control)
  - [3.7 Release Management and Delivery](#37-release-management-and-delivery)
- [4. SCM Schedules](#4-scm-schedules)
- [5. SCM Resources](#5-scm-resources)
- [6. SCM Plan Maintenance](#6-scm-plan-maintenance)
- [Appendix A. Conformance Declaration](#appendix-a-conformance-declaration)

---

## 1. Introduction

### 1.1 Purpose

> **Guidance:** State briefly why this Plan exists and describe its intended audience.

*[Enter text here.]*

### 1.2 Scope

> **Guidance:** Address SCM applicability, limitations, and assumptions on which the Plan is based. Include:

- Overview description of the software project
- Identification of the software configuration item(s) (CIs) to which SCM applies
- Identification of other software included in the Plan (e.g., support or test software)
- Relationship of SCM to hardware- or system-level configuration management for the project
- Degree of formality, depth of control, and portion of the life cycle over which SCM applies
- Limitations (e.g., time constraints) that apply to the Plan
- Assumptions that could affect the cost, schedule, or ability to perform the defined SCM activities

*[Enter text here.]*

### 1.3 Definitions, Acronyms, and Abbreviations

> **Guidance:** Define key terms as they apply to this Plan, or reference a project glossary, so all users share common terminology.

| Term / Acronym | Definition |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |

### 1.4 References

> **Guidance:** Uniquely identify every policy, directive, procedure, standard, and related document referenced in this Plan so users can retrieve it.

| Document ID | Title | Version / Date |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

---

## 2. SCM Management

### 2.1 Organization

> **Guidance:** Describe the technical and managerial organizational context for the planned SCM activities. Identify:

- All organizational units that participate in or are responsible for any SCM activity on the project
- All organizational units that participate in or are responsible for the problem-resolution process
- The functional roles of these organizational units within the project structure
- Relationships between organizational units and the interfaces implementing those relationships

> **Note:** An organization chart, supplemented by statements of function, role, and relationship, is an effective way to present this information.

*[Enter text here.]*

### 2.2 SCM Responsibilities

> **Guidance:** Allocate each SCM activity from Section 3 to a responsible organizational unit or job title. For any review board or CCB, describe its purpose/objectives, membership and affiliations, period of effectivity, scope of authority, and operating procedures. Identify any external constraints on the Plan (from other policies, directives, or procedures) and state their impact.

| SCM Activity (§3 reference) | Responsible Organization / Role |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |

### 2.3 Applicable Policies, Directives, and Procedures

> **Guidance:** List the external policies, directives, and procedures that place constraints on this Plan, and state the impact/effect of each.

*[Enter text here.]*

### 2.4 Management of the SCM Process

> **Guidance:** Identify the organizational unit responsible for the overall SCM process, and describe or reference:

- The anticipated cost of the SCM process and the means for periodically monitoring planned vs. actual costs
- The means for, and organizational unit responsible for, independent surveillance of SCM activities to ensure compliance with this Plan
- The identification, assessment, and mitigation plans for risks associated with performing the SCM activities (technical, economic, schedule, managerial)

*[Enter text here.]*

---

## 3. SCM Activities

### 3.1 Configuration Identification

> **Guidance:** Identify, name, and describe the documented physical and functional characteristics of the code, specifications, design, and data elements to be controlled for the project.

#### 3.1.1 Identifying Configuration Items

> **Guidance:** Record the items to be controlled (the project CIs) and describe how the list of items and structures are maintained. Define how baselines are created, in terms of:

- The event that creates the baseline
- The items that are to be controlled in the baseline
- The procedures used to establish and change the baseline
- The authority required to approve changes to the approved baselined documents

> **Note:** Also specify how changes are identified and associated with the affected CIs and related baseline.

*[Enter text here.]*

#### 3.1.2 Naming Configuration Items

> **Guidance:** Specify an identification system for assigning unique identifiers to each controlled item and to each version. Describe the naming methods used for storage, retrieval, tracking, reproduction, and distribution.

*[Enter text here.]*

#### 3.1.3 Acquiring Configuration Items

> **Guidance:** Identify the controlled software libraries and describe how baselined code, documentation, and data are placed under control. Address:

- Format, location, documentation requirements, receiving/inspection requirements, and access control for each library
- Storage procedures, including physical marking/labeling, retention periods, and disaster prevention/recovery
- Procedures for retrieving and reproducing controlled items, including marking verification, copy tracking, and protection of proprietary/security information

*[Enter text here.]*

### 3.2 Configuration Control

> **Guidance:** Describe the change controls imposed on baselined CIs for each project software library, defining the sequence of steps below, and identify the records used to track and document each change.

#### 3.2.1 Requesting Changes

> **Guidance:** Specify the procedure for requesting a change to a baselined CI. As a minimum, record:

- The name(s) and version(s) of the CI(s) where the change is desired
- Originator's name and organization
- Date of request
- Indication of urgency
- The need for the change
- Description of the requested change

*[Enter text here.]*

#### 3.2.2 Evaluating Changes

> **Guidance:** Specify the analysis required to determine the impact of a proposed change (effect on the deliverable and on project resources) and the procedures for reviewing the results of that analysis.

*[Enter text here.]*

#### 3.2.3 Approving or Disapproving Changes

> **Guidance:** Identify each configuration control board (CCB) and its level of authority for approving proposed changes. If multiple CCBs are used, specify how the proper level is determined for a given change request.

*[Enter text here.]*

#### 3.2.4 Implementing Changes

> **Guidance:** Specify the activities for verifying and implementing an approved change. As a minimum, record:

- The associated change request(s)
- The names and versions of the affected items
- Verification date and responsible party
- Release or installation date and responsible party
- The identifier of the new version

> **Note:** Also specify activities for release planning and control (e.g., coordinating multiple changes, reconfiguring CIs, delivering a new baseline).

*[Enter text here.]*

### 3.3 Configuration Status Accounting

> **Guidance:** Describe how the status of project CIs is recorded and reported. Address:

- What data elements and SCM metrics are tracked and reported for baselines and changes
- What types of status accounting reports are generated, and their frequency
- How information is collected, stored, processed, reported, and protected from loss
- How access to the status data is controlled

> **Note:** As a minimum, track and report each CI's approved versions, the status of requested changes, and the implementation status of approved changes.

*[Enter text here.]*

### 3.4 Configuration Evaluation and Reviews

> **Guidance:** Identify the configuration audits and reviews to be held (at minimum, a configuration audit prior to each CI's release). For each planned audit or review, define:

- Its objective
- The CIs under audit or review
- The schedule of audit or review tasks
- The procedures for conducting the audit or review
- The participants, by job title
- Documentation required to be available
- The procedure for recording deficiencies and reporting corrective actions
- The approval criteria and the specific action(s) to occur upon approval

*[Enter text here.]*

### 3.5 Interface Control

> **Guidance:** Identify the external items to which the project software interfaces. For each interface, define:

- The nature of the interface
- The affected organizations
- How the interface code, documentation, and data are controlled
- How interface control documents are approved and released into a specified baseline

> **Note:** If a CCB is established to control interfaces, identify its responsibilities and procedures (see §2.2).

*[Enter text here.]*

### 3.6 Subcontractor/Vendor Control

> **Guidance:** Define the activities used to incorporate externally developed items into the project CIs and to coordinate changes with their development organizations. For subcontracted software, describe:

- What SCM requirements (including an SCM Plan) are part of the subcontractor's agreement
- How the subcontractor will be monitored for compliance
- What configuration evaluations and reviews of subcontractor items will be held
- How external code, documentation, and data will be tested, verified, accepted, and merged with the project software
- How proprietary items will be handled for security of information and traceability of ownership
- How changes are to be processed, including the subcontractor's participation

> **Note:** For acquired software, describe how it will be received, tested, and placed under SCM; how changes to the supplier's software are processed; and whether/how the supplier participates in change management.

*[Enter text here.]*

### 3.7 Release Management and Delivery

> **Guidance:** Describe how the build, release, and delivery of software products and documentation will be formally controlled, including procedures for approved deviations and waivers, retention of master copies for the life of the product, and handling of safety- or security-critical code and documentation.

*[Enter text here.]*

---

## 4. SCM Schedules

> **Guidance:** State the sequence and dependencies among all SCM activities, and the relationship of key SCM activities to project milestones or events. The schedule shall cover the duration of the Plan and contain all major SCM-related milestones, including establishment of a configuration baseline, implementation of change-control procedures, and the start and completion dates of each configuration audit.

> **Note:** Express dates as absolute dates, dates relative to SCM or project milestones, or a simple sequence of events. A graphic (e.g., Gantt chart) is often the clearest way to convey this information.

| SCM Activity / Milestone | Dependency | Target Date |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

---

## 5. SCM Resources

> **Guidance:** Identify the environment, infrastructure, software tools, techniques, equipment, personnel, and training necessary to execute the SCM activities defined in Section 3. Address:

- The infrastructure needed for SCM (functionality, performance, safety, security, availability, space, equipment, cost, time) and how the infrastructure itself is kept under configuration management
- For each SCM activity: what tools, techniques, equipment, personnel, and training are required, and how each resource will be provided or obtained
- For each software tool (developed in-project or brought in from outside): its function, and the configuration controls placed on the tool itself

*[Enter text here.]*

---

## 6. SCM Plan Maintenance

> **Guidance:** Identify the activities and responsibilities needed to keep this Plan current through the project life cycle. State:

- Who is responsible for monitoring the Plan
- How frequently updates are performed
- How changes to the Plan are evaluated and approved
- How changes to the Plan are made and communicated

> **Note:** Maintain a history of changes made to this Plan (see the Revision History table above). Review the Plan at the start of each project phase, update as needed, and re-distribute to the project team.

*[Enter text here.]*

---

## Appendix A. Conformance Declaration

> **Guidance:** Complete this checklist before declaring conformance with IEEE Std 828-2005 (see Clause 5 of the standard).

- All six classes of SCM information are present: Introduction, SCM Management, SCM Activities, SCM Schedules, SCM Resources, and SCM Plan Maintenance
- Every required item ("shall" / "required") in each class is documented, or its omission is justified in the Introduction (see §1.2)
- This document (or a clearly labeled section) is titled "Software Configuration Management Plan" and contains all SCM planning information, by inclusion or by reference
- Every activity defined in §3.1–3.7 is assigned to an organizational unit (§2.2)
- Every activity defined has resources identified to accomplish it (§5)
- Every CI identified in §3.1 has a defined process for baseline establishment and change control (§3.2)

If every item above is satisfied, this Plan may include the following declaration:

> *"This SCM Plan conforms with the requirements of IEEE Std 828-2005."*
