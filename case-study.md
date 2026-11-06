# Case study — bilingual higher-education CMS

## Executive summary

OSYSTIC developed a PHP/MariaDB college administration system with a bilingual Arabic/English interface and permission-aware workflows across admissions, academics, student services, finance, faculty, quality and learning-related operations. The engineering work included secured records, domain validation and technical release checks. This sanitized case study describes a production technical-verification checkpoint; it does **not** assert final college acceptance, complete external provider activation or clearance to disclose client systems.

## Challenge

Seven institutional workstreams needed a coherent record-and-workflow model: admissions, academic administration, students, finance, faculty, quality, and learning/executive operations. A partial collection of pages would not be enough. Cross-module data consistency, operator permissions, traceability, bilingual usability and deployability had to be treated as system concerns.

## Solution

**1. Layered application architecture.** A server-rendered web experience backed by services and a relational database. Controllers handle requests; service boundaries validate rules; domain models and reports operate on structured records.

**2. Restricted workflows.** Role-based access ensures that publicly accessible application/tracking pages are separate from internal student, staff, reporting and document operations. Negative authorization checks, session handling and CSRF checks are part of the test strategy.

**3. Bilingual design.** Explicit English/Arabic catalogs, RTL-aware layouts, labels and error messages. Application data and personal names are not blindly rewritten by translation logic.

**4. Operational integrity.** The application enforces admissions catalog relationships and selected academic workflow constraints. Sensitive files are stored outside publicly served paths. Reports and backup verification are treated as release concerns.

**5. External API boundaries.** Optional education, communication, payment and AI services have adapter boundaries, with credentials and policy approval held outside source control. This separates integration readiness from production connection claims.

## Technologies

PHP 8.2+, MariaDB/MySQL, SQL migrations, HTML, CSS, JavaScript, bilingual interface catalogs, PDF/document generation, Python-assisted QA, Git and CI workflows.

## Engineering and validation

The private release evidence includes automated PHP regression, browser flows for English/Arabic and different device widths, negative-access cases, schema and backup preflight, and deployed-source consistency checks. This public artifact publishes only the test methodology and defensible technical status, not private fixtures or institution-identifying evidence.

## Outcome

A production-deployed CMS application architecture with multi-module business workflows and a clear separation between implementation success, external-provider readiness and institutional acceptance. The engagement's reusable lesson is **explicit permissions + deterministic service validation + bilingual QA + reversible releases**.

## Ownership and handover boundary

The original source, internal databases, credentials, institution-specific policies, production access, release records and operator documentation remain outside this public companion. Public disclosure of architecture patterns is not equivalent to source delivery, intellectual-property assignment or a signed institutional handover. Private approvals and the institution's pending acceptance tasks must be verified independently.

The accompanying [conceptual architecture illustration](assets/campus-system-concept.svg) depicts service boundaries rather than a captured production screen or verified deployment topology.

## Boundaries

This is a sanitized narrative. It is not a demo system, production support portal, client reference authorization, database export, or transferable source license. The private solution and institutional data are not disclosed.
