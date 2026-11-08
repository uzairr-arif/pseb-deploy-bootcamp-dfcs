<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&height=190&text=Digital%20Forensics%20%26%20Cyber%20Security&desc=SC-500%20Weekend%20Bootcamp%20%C2%B7%20PSEB%20DEPLOY%20%C2%B7%20Atomcamp&color=0:0F2D44,100:17A398&textColor=ffffff&descColor=d6e4f7&section=header" width="100%" />

# DFCS Bootcamp Portfolio

**Muhammad Uzair Arif** · Cohort `02-Weekend-ISB`

<img src="https://img.shields.io/badge/BY-PSEB_DEPLOY-01411C?style=for-the-badge" alt="A PSEB DEPLOY initiative" />
<img src="https://img.shields.io/badge/TRAINED_BY-ATOMCAMP-FF6B35?style=for-the-badge" alt="Trained by Atomcamp" />
<img src="https://img.shields.io/badge/SC_500-CERTIFICATION_BY_PSEB-1F4E79?style=for-the-badge" alt="SC-500 certification by PSEB" />

<img src="https://img.shields.io/badge/track-Digital_Forensics_%26_Cyber_Security-0F2D44?style=flat-square" alt="Track" />
<img src="https://img.shields.io/badge/duration-3_Months_Weekend_Cohort-17A398?style=flat-square" alt="Duration" />
<img src="https://img.shields.io/badge/assignments-3_of_4-2E74B5?style=flat-square" alt="Assignments" />
<img src="https://img.shields.io/badge/status-In_Progress-FFB300?style=flat-square" alt="Status" />

<img src="https://img.shields.io/badge/Kali_Linux-attacker_vm-5586A5?style=flat-square&logo=kalilinux&logoColor=white" alt="Kali Linux" />
<img src="https://img.shields.io/badge/Metasploitable_2-target_vm-8B0000?style=flat-square&logo=virtualbox&logoColor=white" alt="Metasploitable 2" />
<img src="https://img.shields.io/badge/Nmap-7.95-21759B?style=flat-square&logo=nmap&logoColor=white" alt="Nmap" />
<img src="https://img.shields.io/badge/Metasploit-msf6-2596BE?style=flat-square&logo=metasploit&logoColor=white" alt="Metasploit" />
<img src="https://img.shields.io/badge/GVM_OpenVAS-vulnerability_scanning-3E7BFA?style=flat-square&logo=openvas&logoColor=white" alt="OpenVAS" />
<img src="https://img.shields.io/badge/OpenSSL-3.x-7A1FA2?style=flat-square&logo=openssl&logoColor=white" alt="OpenSSL" />
<img src="https://img.shields.io/badge/Python-3-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/VirtualBox-isolated_NAT_lab-183A61?style=flat-square&logo=virtualbox&logoColor=white" alt="VirtualBox" />

</div>

---

## About this repository

This is the submission portfolio for the **Digital Forensics & Cyber Security (DFCS) weekend bootcamp**, a **PSEB DEPLOY** initiative by the **Pakistan Software Export Board (PSEB)**, delivered through **Atomcamp**. Every assignment is submitted here as Markdown with terminal evidence, and on successful completion of the programme PSEB covers the **SC-500 certification**.

Every claim in the assignments follows the course standard: each one is backed by a command, a screenshot or a cited source. All hands-on work was performed against my own isolated lab, never against systems I do not own.

## Programme

| | |
|---|---|
| **Initiative** | PSEB DEPLOY (Pakistan Software Export Board) |
| **Training partner** | Atomcamp |
| **Track** | SC-500 - Digital Forensics & Cyber Security |
| **Format** | Weekend cohort, approximately 3 months |
| **Certification** | SC-500 by PSEB on programme completion |
| **Trainer** | Waseem Abbas Khan (Senior Cybersecurity Specialist, CEI Master Trainer) |

## Course outline and progress

The trainer publishes each weekend's handout in turn; the table below tracks every session and links its submission folder. Topics for the remaining weekends are filled in as the handouts are released.

| Module | Topic | Status | Submission |
|:---:|---|:---:|:---:|
| **S01** | Foundations: information security, Linux, files and permissions, networking, ciphers and encryption | ![done](https://img.shields.io/badge/completed-2E7D32?style=flat-square) | [s01-foundations](s01-foundations/) |
| **S06** | Network, Port and Vulnerability Scanning (Nmap, NSE, CVE/CVSS/CWE research) | ![done](https://img.shields.io/badge/completed-2E7D32?style=flat-square) | [s06-scanning](s06-scanning/) |
| **S07** | From Vulnerability Scanning to Exploitation and Reporting (GVM/OpenVAS, Metasploit, VA/PT report) | ![in progress](https://img.shields.io/badge/in_progress-FFB300?style=flat-square) | [s07-report](s07-report/) |
| **S02** | Upcoming - announced per weekend | ![upcoming](https://img.shields.io/badge/pending-9AA7B0?style=flat-square) | - |
| **S03** | Upcoming - announced per weekend | ![upcoming](https://img.shields.io/badge/pending-9AA7B0?style=flat-square) | - |
| **S04** | Upcoming - announced per weekend | ![upcoming](https://img.shields.io/badge/pending-9AA7B0?style=flat-square) | - |
| **S05** | Upcoming - announced per weekend | ![upcoming](https://img.shields.io/badge/pending-9AA7B0?style=flat-square) | - |
| **S08+** | Upcoming - announced per weekend | ![upcoming](https://img.shields.io/badge/pending-9AA7B0?style=flat-square) | - |

Topics the handouts have already announced for later weekends: operating systems in depth and Windows event logs, malware analysis on isolated networks, detection and SOC workflows, privilege escalation, and digital forensics evidence handling.

## Assignments

| # | Assignment | Tasks completed | Status |
|:---:|---|---|:---:|
| 1 | Foundations homework | Task A (malware research) · B2 (file permissions) · B4 (OpenSSL and `Salted__`) | ![submitted](https://img.shields.io/badge/submitted-2E7D32?style=flat-square) |
| 2 | Scanning homework | Task A (three findings) · B1 (discovery tools) · B3 (CVSS decode) | ![submitted](https://img.shields.io/badge/submitted-2E7D32?style=flat-square) |
| 3 | VA/PT report | Full report (4 findings) · GVM comparison · Metasploit write-up | ![in progress](https://img.shields.io/badge/in_progress-FFB300?style=flat-square) |
| 4 | To be announced | - | ![upcoming](https://img.shields.io/badge/pending-9AA7B0?style=flat-square) |

## Lab environment

| Role | Operating system | Network |
|---|---|---|
| Attacker | Kali Linux | isolated VirtualBox NAT segment |
| Target | Metasploitable 2 (VulnHub) | same isolated segment |

Metasploitable 2 is an intentionally vulnerable training machine from VulnHub, kept on an isolated NAT segment so it is unreachable from any real network. Every technique in this portfolio was executed against my own lab only.

## Repository structure

```text
pseb-deploy-bootcamp-dfcs/
├── README.md                    this programme overview
├── s01-foundations/             Assignment 1 - submitted
│   ├── README.md                Task A + B2 + B4 with evidence
│   ├── Figures/                 Kali terminal screenshots
│   └── S01_Malware_Research_and_Linux_Practical.docx
├── s06-scanning/                Assignment 2 - submitted
│   ├── README.md                three findings + B1 + B3 with evidence
│   ├── Figures/                 scan evidence (9 captures)
│   └── S06_Network_Port_Vulnerability_Scanning.docx
└── s07-report/                  Assignment 3 - in progress
    ├── README.md                full VA/PT report source
    ├── Figures/  evidence/      exploitation and GVM evidence
    ├── S07_VAPT_Report.docx
    └── S07_VAPT_Report.pdf      formal deliverable
```

## Evidence standards

Standards taken directly from the course handouts and applied to every submission:

- Markdown, in my own words, with screenshots embedded.
- Every assertion supported by a command, a screenshot or a cited source.
- Findings documented with severity (CVSS vector), affected asset, identifiers (CVE/CWE/CPE), reproducible proof of concept, impact and remediation.
- Severity scored honestly: inflated ratings destroy credibility faster than missed findings.

## Responsible use

All scanning and exploitation in this portfolio targets my own Metasploitable 2 VM in an isolated laboratory. Using these techniques against systems without written authorisation is a criminal offence in Pakistan under the **Prevention of Electronic Crimes Act 2016** and in every comparable jurisdiction. The skill being built is the ability to do this lawfully, within a written scope, and to prove afterwards exactly what was done.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:17A398,100:0F2D44&height=90&section=footer" width="100%" />

**A PSEB DEPLOY initiative by the Pakistan Software Export Board · Delivered by Atomcamp · SC-500 certification on completion**

</div>
