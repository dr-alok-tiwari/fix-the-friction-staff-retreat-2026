import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
from io import StringIO

# ============================================================
# Fix the Friction | Staff Retreat 2026 | Streamlit Website
# Local, no API keys, no paid services
# ============================================================

st.set_page_config(
    page_title="Fix the Friction | Staff Retreat 2026",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------
# Theme and CSS
# ----------------------------
PRIMARY = "#12355B"
TEAL = "#00A6A6"
GOLD = "#F2B705"
SAFFRON = "#F28C28"
SOFT_BG = "#F6F8FB"
SOFT_CARD = "#FFFFFF"
MUTED = "#64748B"
GREEN = "#2E8B57"
RED_SOFT = "#F9E8E8"
BLUE_SOFT = "#EAF3FF"
TEAL_SOFT = "#E8F8F7"
GOLD_SOFT = "#FFF7DB"

st.markdown(
    f"""
    <style>
    :root {{
        --primary: {PRIMARY};
        --teal: {TEAL};
        --gold: {GOLD};
        --saffron: {SAFFRON};
        --soft-bg: {SOFT_BG};
        --muted: {MUTED};
    }}
    .block-container {{
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }}
    html, body, [class*="css"] {{
        font-family: "Inter", "Segoe UI", sans-serif;
    }}
    .hero {{
        background: linear-gradient(135deg, #12355B 0%, #0B6E69 55%, #F2B705 140%);
        border-radius: 28px;
        padding: 2.2rem 2.4rem;
        color: white;
        box-shadow: 0 22px 55px rgba(18,53,91,.22);
        position: relative;
        overflow: hidden;
    }}
    .hero:after {{
        content: "";
        position: absolute;
        width: 320px;
        height: 320px;
        border-radius: 999px;
        right: -90px;
        top: -90px;
        background: rgba(255,255,255,.12);
    }}
    .hero h1 {{
        font-size: 3.2rem;
        line-height: 1.02;
        margin: 0 0 .4rem 0;
        letter-spacing: -1px;
    }}
    .hero p {{
        font-size: 1.08rem;
        margin: .35rem 0;
        max-width: 1050px;
    }}
    .mini-badge {{
        display: inline-block;
        background: rgba(255,255,255,.15);
        border: 1px solid rgba(255,255,255,.28);
        border-radius: 999px;
        padding: .38rem .78rem;
        margin: .25rem .25rem .25rem 0;
        color: white;
        font-weight: 700;
        font-size: .84rem;
    }}
    .badge {{
        display: inline-block;
        border-radius: 999px;
        padding: .35rem .72rem;
        font-weight: 750;
        font-size: .78rem;
        margin: .15rem .12rem;
        border: 1px solid rgba(18,53,91,.08);
    }}
    .badge-blue {{ background: #EAF3FF; color: #12355B; }}
    .badge-teal {{ background: #E8F8F7; color: #006B6B; }}
    .badge-gold {{ background: #FFF7DB; color: #8A6300; }}
    .badge-saffron {{ background: #FFF0E3; color: #9A4E00; }}
    .card {{
        background: {SOFT_CARD};
        border: 1px solid rgba(18,53,91,.08);
        border-radius: 22px;
        padding: 1.15rem 1.25rem;
        box-shadow: 0 10px 28px rgba(18,53,91,.08);
        margin-bottom: 1rem;
    }}
    .soft-card {{
        background: linear-gradient(180deg, #ffffff 0%, #F9FBFD 100%);
        border: 1px solid rgba(18,53,91,.08);
        border-radius: 20px;
        padding: 1rem 1.1rem;
        box-shadow: 0 8px 24px rgba(18,53,91,.07);
        min-height: 142px;
    }}
    .metric-card {{
        background: white;
        border-radius: 20px;
        padding: 1rem;
        border: 1px solid rgba(18,53,91,.08);
        box-shadow: 0 8px 22px rgba(18,53,91,.07);
    }}
    .section-title {{
        color: {PRIMARY};
        font-size: 1.75rem;
        font-weight: 850;
        margin: .8rem 0 .2rem 0;
        letter-spacing: -.3px;
    }}
    .section-subtitle {{
        color: {MUTED};
        font-size: 1rem;
        margin-bottom: 1.1rem;
    }}
    .callout {{
        border-left: 6px solid {TEAL};
        background: #F2FCFC;
        padding: .9rem 1rem;
        border-radius: 14px;
        margin: .8rem 0 1rem 0;
        color: #164E63;
    }}
    .progress-card {{
        border-radius: 22px;
        background: white;
        border: 1px solid rgba(18,53,91,.08);
        padding: 1.1rem;
        min-height: 220px;
        box-shadow: 0 8px 24px rgba(18,53,91,.07);
    }}
    .sticky {{
        border-radius: 18px;
        padding: 1rem;
        background: #FFF7DB;
        border: 1px solid rgba(242,183,5,.35);
        box-shadow: 0 8px 18px rgba(18,53,91,.07);
        margin-bottom: .85rem;
        min-height: 120px;
    }}
    .small-muted {{ color: {MUTED}; font-size: .88rem; }}
    .owner-chip {{
        display: inline-block;
        background: #EEF2FF;
        color: #233876;
        border-radius: 999px;
        padding: .25rem .58rem;
        margin-top: .3rem;
        font-size: .76rem;
        font-weight: 750;
    }}
    .big-number {{
        font-size: 2.2rem;
        color: {PRIMARY};
        font-weight: 900;
        letter-spacing: -1px;
    }}
    .footer-note {{
        color: {MUTED};
        font-size: .86rem;
        border-top: 1px solid rgba(18,53,91,.1);
        margin-top: 2rem;
        padding-top: 1rem;
    }}
    div[data-testid="stMetricValue"] {{ color: {PRIMARY}; }}
    div[data-testid="stSidebar"] {{ background: #F8FAFC; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Data
# ----------------------------

def build_issue_data() -> pd.DataFrame:
    records = [
        # Admissions and Outreach
        {
            "category": "Admissions and Outreach", "department": "Admissions", "theme": "System Coordination",
            "friction_point": "Multiple systems make coordination complex and less efficient.",
            "constructive_reframe": "Admissions workflows can benefit from better system integration and a clearer single point of process visibility.",
            "root_cause": "Information is spread across multiple systems and handover points.",
            "impact": "More time is spent reconciling information, especially during high-demand periods.",
            "quick_win": "Create a simple shared status tracker for priority admissions tasks and pending handovers.",
            "long_term_solution": "Move toward an integrated admissions workflow dashboard with role-wise visibility.",
            "impact_score": 5, "feasibility_score": 4, "urgency_score": 5, "severity_score": 4,
            "suggested_kpi": "Percentage of priority tasks visible in a shared tracker", "timeline": "30 Days", "owner_placeholder": "Admissions + IT Liaison"
        },
        {
            "category": "Admissions and Outreach", "department": "Admissions", "theme": "Workload Pressure",
            "friction_point": "Rising demand and peak-period workload create pressure on existing resources.",
            "constructive_reframe": "Peak-period planning can be strengthened through workload forecasting, task batching, and temporary support models.",
            "root_cause": "Workload peaks are predictable, but resource planning and buffer capacity are limited.",
            "impact": "Critical tasks may take longer, and response quality may be affected during peak windows.",
            "quick_win": "Prepare a peak-period task calendar with daily priority bands and escalation points.",
            "long_term_solution": "Build a seasonal workload model and define peak-period support protocols.",
            "impact_score": 5, "feasibility_score": 3, "urgency_score": 5, "severity_score": 5,
            "suggested_kpi": "Average response time during admissions peak period", "timeline": "60 Days", "owner_placeholder": "Admissions Lead"
        },
        {
            "category": "Admissions and Outreach", "department": "Admissions", "theme": "Communication Responsiveness",
            "friction_point": "Unanswered emails and missed calls can affect responsiveness.",
            "constructive_reframe": "Communication reliability can be improved through shared inbox norms, response ownership, and escalation windows.",
            "root_cause": "High multitasking and unclear ownership of inbound communication channels.",
            "impact": "Stakeholders may experience avoidable waiting time or repeated follow-ups.",
            "quick_win": "Define response-time bands for email and phone queries during critical periods.",
            "long_term_solution": "Adopt a lightweight ticketing or shared inbox workflow for recurring queries.",
            "impact_score": 4, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Percentage of queries responded to within defined TAT", "timeline": "30 Days", "owner_placeholder": "Admissions Operations"
        },
        {
            "category": "Admissions and Outreach", "department": "Admissions", "theme": "Data Retrieval",
            "friction_point": "Retrieving large volumes of data for cross-functional needs remains challenging.",
            "constructive_reframe": "Cross-functional data support can improve through common data dictionaries and reusable reports.",
            "root_cause": "Data formats and retrieval logic are not standardized for recurring institutional needs.",
            "impact": "Repeated manual effort is needed for accreditation, reporting, and internal analysis.",
            "quick_win": "Identify top 10 recurring data requests and create reusable export templates.",
            "long_term_solution": "Create a controlled institutional data mart for recurring reports.",
            "impact_score": 5, "feasibility_score": 3, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Number of recurring reports generated from standardized templates", "timeline": "90 Days", "owner_placeholder": "Admissions + Accreditation + IT"
        },
        # Accounts
        {
            "category": "Accounts and Approvals", "department": "Accounts", "theme": "Approval Visibility",
            "friction_point": "Approval status may remain unclear when approvals are buried inside email threads.",
            "constructive_reframe": "Approval workflows can become faster and more transparent through a visible confirmation mechanism.",
            "root_cause": "Approvals are communicated informally across email chains rather than in a shared status system.",
            "impact": "Repeated follow-ups are needed, increasing manual effort and closure time.",
            "quick_win": "Use a common approval-status template: Pending, Approved, Query Raised, Closed.",
            "long_term_solution": "Adopt a system-based approval workflow with audit trail and stakeholder visibility.",
            "impact_score": 5, "feasibility_score": 5, "urgency_score": 5, "severity_score": 4,
            "suggested_kpi": "Reduction in approval-related follow-ups", "timeline": "30 Days", "owner_placeholder": "Accounts + Requesting Departments"
        },
        {
            "category": "Accounts and Approvals", "department": "Accounts", "theme": "Turnaround Expectations",
            "friction_point": "Last-minute requests disrupt planned work and can affect accuracy.",
            "constructive_reframe": "Advance planning and mutually agreed turnaround expectations can improve accuracy and reduce pressure.",
            "root_cause": "Urgency definitions and minimum submission windows are not consistently visible.",
            "impact": "Planned work gets interrupted, increasing stress and error risk.",
            "quick_win": "Define standard TAT categories and an urgent-request protocol.",
            "long_term_solution": "Create a request calendar and automated reminder workflow for recurring activities.",
            "impact_score": 5, "feasibility_score": 4, "urgency_score": 5, "severity_score": 4,
            "suggested_kpi": "Percentage of requests received within agreed lead time", "timeline": "30 Days", "owner_placeholder": "Accounts + All Departments"
        },
        {
            "category": "Accounts and Approvals", "department": "Accounts", "theme": "Duplicate Effort",
            "friction_point": "The same data may need to be prepared and entered repeatedly across formats or systems.",
            "constructive_reframe": "Single-entry formats can reduce manual effort and improve accuracy across downstream outputs.",
            "root_cause": "Systems and report formats are not sufficiently integrated.",
            "impact": "Time is spent on repeated entry, and the possibility of errors increases.",
            "quick_win": "Create one master input template that feeds multiple required output formats.",
            "long_term_solution": "Integrate recurring accounts workflows through automation or workflow software.",
            "impact_score": 4, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Number of duplicate-entry steps eliminated", "timeline": "60 Days", "owner_placeholder": "Accounts + IT"
        },
        # Accreditation
        {
            "category": "Accreditation, Ranking, and AoL", "department": "Accreditation/AoL", "theme": "Data Timeliness",
            "friction_point": "Data submission for accreditation, ranking, and AoL can be made more timely and visible.",
            "constructive_reframe": "A shared submission calendar and dashboard can improve preparedness and coordination.",
            "root_cause": "Timelines, pending inputs, and responsible owners are not always visible to everyone involved.",
            "impact": "Consolidation becomes slower, especially close to reporting deadlines.",
            "quick_win": "Create a shared data-submission tracker with deadline, owner, and status columns.",
            "long_term_solution": "Build an institutional reporting dashboard for accreditation, ranking, and AoL data flows.",
            "impact_score": 5, "feasibility_score": 5, "urgency_score": 5, "severity_score": 5,
            "suggested_kpi": "Percentage of required inputs received before deadline", "timeline": "30 Days", "owner_placeholder": "Accreditation/AoL + Program Offices"
        },
        {
            "category": "Accreditation, Ranking, and AoL", "department": "Accreditation/AoL", "theme": "SOP Standardization",
            "friction_point": "Data collection and storage practices can be standardized further through SOPs.",
            "constructive_reframe": "Common SOPs and templates can improve consistency, traceability, and readiness.",
            "root_cause": "Departments may use different formats, naming conventions, and storage practices.",
            "impact": "Manual reconciliation and clarification effort increases during reporting cycles.",
            "quick_win": "Create a one-page SOP for each recurring data submission process.",
            "long_term_solution": "Develop a central SOP repository with version control and review cycles.",
            "impact_score": 5, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Number of recurring submissions covered by approved SOPs", "timeline": "60 Days", "owner_placeholder": "Accreditation/AoL Team"
        },
        {
            "category": "Accreditation, Ranking, and AoL", "department": "Accreditation/AoL", "theme": "Assessment Data Quality",
            "friction_point": "CLO/CG attainment calculation is delayed when sub-question-wise marks are not received.",
            "constructive_reframe": "Assessment reporting can improve through clearer sub-question-wise submission protocols and standardized templates.",
            "root_cause": "Faculty submissions may contain total marks only, while AoL mapping requires sub-question-wise details.",
            "impact": "Accurate CLO/CG calculation and reporting take longer than needed.",
            "quick_win": "Provide a locked, pre-mapped marks template before assessment submission.",
            "long_term_solution": "Automate attainment calculation from standardized assessment templates.",
            "impact_score": 5, "feasibility_score": 4, "urgency_score": 5, "severity_score": 5,
            "suggested_kpi": "Percentage of assessment files submitted in correct sub-question-wise format", "timeline": "30 Days", "owner_placeholder": "AoL + Faculty + Program Office"
        },
        # Projects
        {
            "category": "Projects and Infrastructure", "department": "Projects", "theme": "Requirement Clarity",
            "friction_point": "Requirements sometimes change after planning, creating deadline pressure.",
            "constructive_reframe": "Early requirement freezing and change-control checkpoints can improve project predictability.",
            "root_cause": "Initial requirements may not fully capture downstream needs or later changes.",
            "impact": "Project teams need to absorb additional work within the same timeline.",
            "quick_win": "Introduce a requirement sign-off checklist before execution begins.",
            "long_term_solution": "Adopt formal project-change logs with impact on scope, cost, and timeline.",
            "impact_score": 5, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Number of post-freeze requirement changes per project", "timeline": "60 Days", "owner_placeholder": "Projects + User Departments"
        },
        {
            "category": "Projects and Infrastructure", "department": "Projects", "theme": "Cross-Department Support",
            "friction_point": "Fast-track projects require stronger and earlier support from concerned departments.",
            "constructive_reframe": "Fast-track work can benefit from a pre-defined support protocol and clear department-wise handover expectations.",
            "root_cause": "Support expectations may not be communicated early enough or tracked visibly.",
            "impact": "Execution timelines become compressed, especially for urgent infrastructure work.",
            "quick_win": "Create a fast-track project coordination sheet with daily/weekly action owners.",
            "long_term_solution": "Form cross-functional project squads for time-sensitive infrastructure initiatives.",
            "impact_score": 4, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Percentage of fast-track action items closed on time", "timeline": "30 Days", "owner_placeholder": "Projects + Concerned Departments"
        },
        {
            "category": "Projects and Infrastructure", "department": "Projects", "theme": "External Dependency",
            "friction_point": "Consultant design development and statutory approvals can consume significant time.",
            "constructive_reframe": "External dependency risks can be managed through buffer planning, milestone tracking, and early escalation.",
            "root_cause": "Design iterations and multi-stage approvals depend on external timelines.",
            "impact": "Execution windows reduce when design and approval stages take longer.",
            "quick_win": "Maintain a milestone risk tracker for consultants and statutory approval stages.",
            "long_term_solution": "Create a project governance dashboard with external-dependency alerts.",
            "impact_score": 4, "feasibility_score": 3, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Milestones delayed due to external dependencies", "timeline": "90 Days", "owner_placeholder": "Projects Team"
        },
        # IT
        {
            "category": "IT and Digital Workflows", "department": "IT", "theme": "Workload and Manpower",
            "friction_point": "Workload is high relative to available manpower.",
            "constructive_reframe": "IT service planning can be strengthened through workload visibility, ticket prioritization, and planned support windows.",
            "root_cause": "Academic and administrative requests compete with limited team capacity.",
            "impact": "Turnaround time may increase when many requests arrive together.",
            "quick_win": "Classify requests as critical, high, normal, and planned with visible expected response times.",
            "long_term_solution": "Adopt a ticketing system with service categories, SLA targets, and workload dashboards.",
            "impact_score": 5, "feasibility_score": 4, "urgency_score": 5, "severity_score": 5,
            "suggested_kpi": "Average ticket closure time by request category", "timeline": "30 Days", "owner_placeholder": "IT Department"
        },
        {
            "category": "IT and Digital Workflows", "department": "IT", "theme": "Unplanned Requests",
            "friction_point": "Unanticipated urgent tasks disrupt planned IT activities.",
            "constructive_reframe": "Planned and urgent work can be balanced through a visible request pipeline and escalation criteria.",
            "root_cause": "Urgent requests may bypass planning without defined escalation rules.",
            "impact": "Scheduled activities and preventive work may be delayed.",
            "quick_win": "Create a weekly IT request board with urgent-request rules.",
            "long_term_solution": "Institutionalize a demand-management process for recurring digital needs.",
            "impact_score": 4, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Ratio of planned vs unplanned IT requests", "timeline": "60 Days", "owner_placeholder": "IT + Requesting Units"
        },
        {
            "category": "IT and Digital Workflows", "department": "IT", "theme": "Role Clarity",
            "friction_point": "Role overlap can create duplication or accountability gaps.",
            "constructive_reframe": "Clear role mapping can improve task ownership, escalation, and service closure.",
            "root_cause": "Some responsibilities and approval pathways are not fully documented.",
            "impact": "Tasks may be repeated, delayed, or left without clear closure responsibility.",
            "quick_win": "Create a role-responsibility matrix for recurring IT services.",
            "long_term_solution": "Publish a service catalogue with owner, backup owner, TAT, and escalation path.",
            "impact_score": 4, "feasibility_score": 5, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Percentage of recurring services with named owner and backup", "timeline": "30 Days", "owner_placeholder": "IT Department"
        },
        # Library
        {
            "category": "Library and Knowledge Services", "department": "Library", "theme": "Workload Distribution",
            "friction_point": "Workload distribution may become uneven when efficient staff absorb more tasks.",
            "constructive_reframe": "Workload visibility and skill-aligned task allocation can support fairer distribution and stronger motivation.",
            "root_cause": "Task allocation, skill gaps, and completion timelines are not always visible in one place.",
            "impact": "Sincere staff may feel overburdened, and overall morale may be affected.",
            "quick_win": "Create a weekly workload board showing task owner, deadline, and status.",
            "long_term_solution": "Adopt a task-allocation and skill-development plan with periodic review.",
            "impact_score": 4, "feasibility_score": 5, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Percentage of tasks distributed through visible workload board", "timeline": "30 Days", "owner_placeholder": "Library Lead"
        },
        {
            "category": "Library and Knowledge Services", "department": "Library", "theme": "Skill and Software Readiness",
            "friction_point": "Software or skill gaps can create dependency on a few staff members.",
            "constructive_reframe": "Targeted skill-building can reduce dependency and improve service continuity.",
            "root_cause": "Some tools and processes may not have sufficient cross-training.",
            "impact": "Work can concentrate around a few people, increasing delay risk.",
            "quick_win": "Run short peer-learning sessions for common library software workflows.",
            "long_term_solution": "Create a skill matrix and training calendar for critical library processes.",
            "impact_score": 4, "feasibility_score": 4, "urgency_score": 4, "severity_score": 4,
            "suggested_kpi": "Number of staff cross-trained on critical workflows", "timeline": "60 Days", "owner_placeholder": "Library + HR/Training"
        },
        {
            "category": "Library and Knowledge Services", "department": "Library", "theme": "Protocol Adherence",
            "friction_point": "Book-ordering protocols can be followed more consistently.",
            "constructive_reframe": "Clearer book-ordering protocols can reduce back-and-forth and protect process fairness.",
            "root_cause": "Submission expectations and approval steps may not be consistently followed by all requesters.",
            "impact": "Library staff may need to manage avoidable clarification cycles.",
            "quick_win": "Share a one-page book-ordering protocol with required fields and timelines.",
            "long_term_solution": "Create a simple digital book-request form with validation fields.",
            "impact_score": 3, "feasibility_score": 5, "urgency_score": 3, "severity_score": 3,
            "suggested_kpi": "Percentage of book requests submitted with complete information", "timeline": "30 Days", "owner_placeholder": "Library + Faculty Requesters"
        },
    ]
    df = pd.DataFrame(records)
    df["priority_score"] = (
        df["impact_score"] * 0.35
        + df["urgency_score"] * 0.25
        + df["severity_score"] * 0.25
        + df["feasibility_score"] * 0.15
    ).round(2)
    return df

DF = build_issue_data()

TOP_BOTTLENECKS = [
    {
        "title": "Standardization and Single Source of Truth",
        "icon": "🗂️",
        "observed": "Several recurring workflows rely on different templates, systems, and submission formats.",
        "why_it_matters": "When formats differ, teams spend extra time reconciling information instead of using it for timely decisions.",
        "root_cause": "Common templates, SOPs, and shared repositories are not uniformly available across processes.",
        "quick_win": "Create 3–5 standard templates for high-frequency workflows such as data submission, approval requests, and assessment reporting.",
        "long_term": "Develop a controlled institutional process repository with single-source dashboards for recurring data needs.",
        "kpi": "Percentage of recurring workflows using approved templates and SOPs",
        "timeline": "30–60 Days",
    },
    {
        "title": "Last-Minute Requests and Turnaround Expectations",
        "icon": "⏱️",
        "observed": "Several teams experience pressure when requests arrive close to deadlines or outside planned work cycles.",
        "why_it_matters": "Urgent work is sometimes unavoidable, but repeated unplanned requests can affect quality, accuracy, and staff well-being.",
        "root_cause": "Clear TAT categories, urgent-request criteria, and advance planning calendars are not always visible.",
        "quick_win": "Define common TAT bands and an urgent-request protocol for recurring administrative tasks.",
        "long_term": "Introduce department-wise planning calendars and request pipelines for seasonal workload peaks.",
        "kpi": "Percentage of requests received within agreed lead time",
        "timeline": "30 Days",
    },
    {
        "title": "Approval, Ownership, and Coordination Visibility",
        "icon": "🧭",
        "observed": "Some workflows slow down because approval status, task ownership, or handover responsibility is not visible to all stakeholders.",
        "why_it_matters": "Visibility reduces repeated follow-ups and helps teams close work with greater confidence.",
        "root_cause": "Approvals, handovers, and accountability points often sit inside email chains or informal conversations.",
        "quick_win": "Use a shared tracker with owner, status, next action, deadline, and escalation route.",
        "long_term": "Move priority workflows to a lightweight ticketing or approval management system.",
        "kpi": "Reduction in repeated follow-ups and average approval closure time",
        "timeline": "30–90 Days",
    },
]

SOLUTIONS = [
    {"solution": "Shared Approval Tracker", "icon": "✅", "problem": "Approval visibility", "ease": "High", "impact": "High", "owner": "Accounts + Departments", "timeline": "30 Days", "kpi": "Follow-ups reduced"},
    {"solution": "Common Data Submission Template", "icon": "📄", "problem": "Inconsistent data formats", "ease": "High", "impact": "High", "owner": "Accreditation/AoL", "timeline": "30 Days", "kpi": "On-time complete submissions"},
    {"solution": "Department-wise SOP Repository", "icon": "📚", "problem": "Unclear process steps", "ease": "Medium", "impact": "High", "owner": "Process Owners", "timeline": "60 Days", "kpi": "SOPs approved and used"},
    {"solution": "30–60 Day TAT Framework", "icon": "⏳", "problem": "Last-minute pressure", "ease": "High", "impact": "High", "owner": "All Departments", "timeline": "30 Days", "kpi": "Requests within lead time"},
    {"solution": "Single-Source Data Dashboard", "icon": "📊", "problem": "Repeated data retrieval", "ease": "Medium", "impact": "Very High", "owner": "IT + Data Owners", "timeline": "90 Days", "kpi": "Reusable reports created"},
    {"solution": "Advance Request Calendar", "icon": "🗓️", "problem": "Unplanned demand", "ease": "High", "impact": "Medium", "owner": "Department Heads", "timeline": "30 Days", "kpi": "Planned vs urgent request ratio"},
    {"solution": "Workload Visibility Board", "icon": "📌", "problem": "Uneven task distribution", "ease": "High", "impact": "Medium", "owner": "Team Leads", "timeline": "30 Days", "kpi": "Task allocation transparency"},
    {"solution": "Cross-Functional Handover Checklist", "icon": "🤝", "problem": "Handover gaps", "ease": "High", "impact": "High", "owner": "Cross-functional Teams", "timeline": "30 Days", "kpi": "Handover rework reduced"},
    {"solution": "Faculty Submission Protocol Reminder", "icon": "🎓", "problem": "Incomplete assessment data", "ease": "High", "impact": "High", "owner": "AoL + Program Office", "timeline": "30 Days", "kpi": "Correct template usage"},
    {"solution": "Monthly Process Review Huddle", "icon": "🔄", "problem": "Low follow-through", "ease": "High", "impact": "Medium", "owner": "Registrar/Team Leads", "timeline": "60 Days", "kpi": "Action closure rate"},
    {"solution": "Automation for Repetitive Entry", "icon": "⚙️", "problem": "Duplicate effort", "ease": "Medium", "impact": "High", "owner": "IT + Process Teams", "timeline": "90 Days", "kpi": "Manual steps eliminated"},
    {"solution": "Digital Ticketing System", "icon": "🎫", "problem": "Request tracking", "ease": "Medium", "impact": "Very High", "owner": "IT + Admin", "timeline": "90 Days", "kpi": "Ticket closure time"},
]

ROADMAP = {
    "First 30 Days": [
        "Finalize top bottlenecks",
        "Create common templates",
        "Define approval visibility process",
        "Draft TAT norms",
        "Identify process owners",
    ],
    "31–60 Days": [
        "Pilot shared dashboard",
        "Run SOP awareness sessions",
        "Start department-wise tracking",
        "Create escalation rules for urgent requests",
        "Standardize recurring data submissions",
    ],
    "61–90 Days": [
        "Review progress",
        "Automate repetitive tasks",
        "Create monthly KPI dashboard",
        "Document lessons learned",
        "Institutionalize best practices",
    ],
}

DEFAULT_KPIS = {
    "Average approval turnaround time": 6,
    "Requests submitted through standard format (%)": 35,
    "Data received on time (%)": 45,
    "Repeated follow-ups reduced (%)": 20,
    "Duplicate-entry steps reduced (%)": 15,
    "SOPs created": 4,
    "Peak-period response time improvement (%)": 10,
    "Staff satisfaction pulse score / 5": 3.6,
    "Cross-functional closure rate (%)": 55,
}

# ----------------------------
# Helpers
# ----------------------------

def section_header(title: str, subtitle: str = ""):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div class='section-subtitle'>{subtitle}</div>", unsafe_allow_html=True)


def score_badge(label, value, color="badge-blue"):
    return f"<span class='badge {color}'>{label}: {value}</span>"


def make_report(filtered_df: pd.DataFrame) -> str:
    timestamp = datetime.now().strftime("%d %b %Y, %I:%M %p")
    out = StringIO()
    out.write("# Fix the Friction: Staff Retreat 2026 Summary Report\n\n")
    out.write(f"Generated on: {timestamp}\n\n")
    out.write("## Purpose\n")
    out.write("This report summarizes process improvement opportunities in a constructive, non-blaming, solution-oriented format.\n\n")
    out.write("## Top 3 Bottlenecks\n")
    for i, item in enumerate(TOP_BOTTLENECKS, 1):
        out.write(f"### {i}. {item['title']}\n")
        out.write(f"- Observation: {item['observed']}\n")
        out.write(f"- Root cause: {item['root_cause']}\n")
        out.write(f"- Quick win: {item['quick_win']}\n")
        out.write(f"- KPI: {item['kpi']}\n\n")
    out.write("## Filtered Friction Points\n")
    for _, row in filtered_df.iterrows():
        out.write(f"### {row['constructive_reframe']}\n")
        out.write(f"- Category: {row['category']}\n")
        out.write(f"- Theme: {row['theme']}\n")
        out.write(f"- Root cause: {row['root_cause']}\n")
        out.write(f"- Quick win: {row['quick_win']}\n")
        out.write(f"- Long-term solution: {row['long_term_solution']}\n")
        out.write(f"- KPI: {row['suggested_kpi']}\n")
        out.write(f"- Timeline: {row['timeline']}\n\n")
    if "ideas" in st.session_state and st.session_state.ideas:
        out.write("## Reflection Wall Inputs\n")
        for idea in st.session_state.ideas:
            out.write(f"- {idea['prompt']}: {idea['text']}\n")
    return out.getvalue()


def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    categories = sorted(df["category"].unique().tolist())
    themes = sorted(df["theme"].unique().tolist())
    timelines = ["30 Days", "60 Days", "90 Days"]

    with st.sidebar:
        st.markdown("### 🔎 Filters")
        selected_categories = st.multiselect("Process areas", categories, default=categories)
        selected_themes = st.multiselect("Themes", themes, default=themes)
        selected_timelines = st.multiselect("Time horizon", timelines, default=timelines)
        min_impact = st.slider("Minimum impact score", 1, 5, 1)
        min_feasibility = st.slider("Minimum feasibility score", 1, 5, 1)

    return df[
        df["category"].isin(selected_categories)
        & df["theme"].isin(selected_themes)
        & df["timeline"].isin(selected_timelines)
        & (df["impact_score"] >= min_impact)
        & (df["feasibility_score"] >= min_feasibility)
    ].copy()


def render_hero():
    st.markdown(
        """
        <div class="hero">
            <span class="mini-badge">Staff Retreat 2026</span>
            <span class="mini-badge">Sub-theme 01</span>
            <span class="mini-badge">Fix the Friction</span>
            <h1>Fix the Friction</h1>
            <p><strong>Turning everyday operational challenges into shared improvement opportunities.</strong></p>
            <p>Main theme: <strong>Break the Barriers: Align, Collaborate, Deliver</strong></p>
            <p>The purpose is not to complain, but to collectively improve how we work, coordinate, and deliver institutional outcomes.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_icon_cards():
    cols = st.columns(6)
    cards = [
        ("🧭", "Clarity", "Make status, ownership, and next actions visible."),
        ("🤝", "Collaboration", "Strengthen handovers across teams."),
        ("⚡", "Speed", "Reduce avoidable waiting and repeated follow-ups."),
        ("📊", "Data", "Standardize templates and reporting flows."),
        ("✅", "Accountability", "Assign owners and track progress respectfully."),
        ("🌱", "Progress", "Convert friction into practical improvement."),
    ]
    for col, (icon, title, desc) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
                <div class="soft-card">
                    <div style="font-size:2rem;">{icon}</div>
                    <h4 style="margin:.25rem 0;color:{PRIMARY};">{title}</h4>
                    <div class="small-muted">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def page_home(filtered_df: pd.DataFrame):
    render_hero()
    st.write("")
    render_icon_cards()
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Process areas", filtered_df["category"].nunique())
    c2.metric("Improvement points", len(filtered_df))
    c3.metric("Quick-win candidates", int((filtered_df["timeline"] == "30 Days").sum()))
    c4.metric("Average priority", round(filtered_df["priority_score"].mean(), 2) if len(filtered_df) else 0)

    st.markdown(
        """
        <div class="callout">
        <strong>Presentation framing:</strong> Every point in this platform is expressed as an improvement opportunity. The goal is to protect dignity, strengthen systems, and help GIM work as one institution and one team.
        </div>
        """,
        unsafe_allow_html=True,
    )

    section_header("Suggested 5–7 Minute Briefing Flow", "Use this website as a structured briefing tool during the retreat presentation.")
    flow_cols = st.columns(5)
    flow = [
        ("1", "Problem", "Clear and specific friction point"),
        ("2", "Root Cause", "Why it happens"),
        ("3", "Solutions", "2–3 practical ideas"),
        ("4", "Implementation", "Owner + action + timeline"),
        ("5", "Learning", "Cross-team insight"),
    ]
    for col, (num, title, desc) in zip(flow_cols, flow):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="big-number">{num}</div>
                <h4 style="color:{PRIMARY}; margin:.1rem 0;">{title}</h4>
                <div class="small-muted">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


def page_context():
    section_header("Retreat Context", "A structured space for reflection, co-creation, and practical action.")
    st.markdown(
        """
        <div class="card">
        <p>The Staff Retreat is positioned as a participatory and solution-oriented exercise. The focus is on understanding operational realities, identifying bottlenecks, and co-creating implementable improvements with shared ownership.</p>
        <p><strong>Sub-theme 01: Fix the Friction</strong> asks: <em>Where do we slow ourselves down—and why?</em></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    cols = st.columns(6)
    steps = [
        ("👂", "Listen", "Gather real inputs"),
        ("🔍", "Understand", "Find root causes"),
        ("🎯", "Prioritize", "Select high-impact issues"),
        ("🛠️", "Solve", "Design practical actions"),
        ("🚀", "Implement", "Assign owner and timeline"),
        ("📈", "Track", "Measure progress"),
    ]
    for col, (icon, title, text) in zip(cols, steps):
        with col:
            st.markdown(f"""
            <div class="soft-card">
                <div style="font-size:2rem;">{icon}</div>
                <h4 style="color:{PRIMARY}; margin:.2rem 0;">{title}</h4>
                <div class="small-muted">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    section_header("Expected Outputs", "Aligned with the retreat agenda and presentation expectations.")
    out_cols = st.columns(4)
    outputs = [
        ("Top 3 Bottlenecks", "Prioritized improvement opportunities"),
        ("Root Causes", "System reasons behind recurring delays"),
        ("Quick Wins", "30–60 day practical actions"),
        ("Accountability", "Owner, timeline, and progress indicator"),
    ]
    for col, (title, text) in zip(out_cols, outputs):
        with col:
            st.markdown(f"<div class='card'><h4 style='color:{PRIMARY};'>{title}</h4><p class='small-muted'>{text}</p></div>", unsafe_allow_html=True)


def page_issue_explorer(filtered_df: pd.DataFrame):
    section_header("Interactive Issue Explorer", "Explore stakeholder inputs using constructive, non-blaming language.")
    if filtered_df.empty:
        st.warning("No records match the selected filters. Please relax the sidebar filters.")
        return

    selected_category = st.selectbox("Choose process area", sorted(filtered_df["category"].unique()))
    local_df = filtered_df[filtered_df["category"] == selected_category]

    st.markdown(f"<span class='badge badge-teal'>Selected area: {selected_category}</span>", unsafe_allow_html=True)
    st.write("")
    for _, row in local_df.sort_values("priority_score", ascending=False).iterrows():
        with st.expander(f"{row['theme']} · {row['constructive_reframe']}", expanded=False):
            c1, c2 = st.columns([1.25, 1])
            with c1:
                st.markdown("#### Constructive framing")
                st.write(row["constructive_reframe"])
                st.markdown("#### Root-cause interpretation")
                st.write(row["root_cause"])
                st.markdown("#### Workflow impact")
                st.write(row["impact"])
            with c2:
                st.markdown("#### Action pathway")
                st.success(f"Quick win: {row['quick_win']}")
                st.info(f"Long-term solution: {row['long_term_solution']}")
                st.markdown(
                    score_badge("Impact", row["impact_score"], "badge-blue")
                    + score_badge("Feasibility", row["feasibility_score"], "badge-teal")
                    + score_badge("Urgency", row["urgency_score"], "badge-gold")
                    + score_badge("Severity", row["severity_score"], "badge-saffron"),
                    unsafe_allow_html=True,
                )
                st.markdown(f"<span class='owner-chip'>Suggested owner: {row['owner_placeholder']}</span>", unsafe_allow_html=True)
                st.caption(f"Suggested KPI: {row['suggested_kpi']} | Timeline: {row['timeline']}")


def page_visual_dashboard(filtered_df: pd.DataFrame):
    section_header("Visual Analytics Dashboard", "Indicative prioritization visuals for structured discussion, not judgment.")
    if filtered_df.empty:
        st.warning("No records match the selected filters.")
        return

    st.markdown("<span class='badge badge-blue'>Scores are discussion indicators only</span><span class='badge badge-teal'>Not performance ratings</span>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        category_counts = filtered_df.groupby("category").size().reset_index(name="count")
        fig = px.bar(
            category_counts,
            x="count", y="category", orientation="h",
            title="Friction Points by Process Area",
            labels={"count": "Number of improvement points", "category": "Process area"},
        )
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=55, b=10))
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        theme_counts = filtered_df.groupby("theme").size().reset_index(name="count")
        fig = px.pie(
            theme_counts,
            names="theme", values="count", hole=.55,
            title="Distribution by Improvement Theme"
        )
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=55, b=10))
        st.plotly_chart(fig, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        dims = ["clarity", "speed", "workload", "standardization", "coordination", "accountability"]
        values = [4.4, 4.2, 4.5, 4.7, 4.3, 4.1]
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=values + [values[0]], theta=dims + [dims[0]], fill="toself", name="Indicative focus"))
        fig.update_layout(
            title="Severity Across Process Dimensions",
            polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
            showlegend=False,
            height=430,
            margin=dict(l=20, r=20, t=55, b=20),
        )
        st.plotly_chart(fig, use_container_width=True)
    with col4:
        heat = pd.pivot_table(filtered_df, values="priority_score", index="category", columns="theme", aggfunc="mean", fill_value=0)
        fig = px.imshow(
            heat,
            text_auto=True,
            aspect="auto",
            title="Process Area × Theme Heatmap",
            labels=dict(color="Priority score"),
        )
        fig.update_layout(height=430, margin=dict(l=10, r=10, t=55, b=10))
        st.plotly_chart(fig, use_container_width=True)

    section_header("30–60–90 Day Implementation Roadmap", "A simple time horizon for visible follow-through.")
    timeline_df = pd.DataFrame({
        "Stage": ["First 30 Days", "31–60 Days", "61–90 Days"],
        "Start": [0, 31, 61],
        "Finish": [30, 60, 90],
        "Focus": ["Templates + owners", "Dashboard + SOP pilot", "Automation + institutionalization"],
    })
    fig = px.timeline(
        timeline_df,
        x_start="Start", x_end="Finish", y="Stage", color="Focus",
        title="Implementation Roadmap"
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(height=330, xaxis_title="Days from retreat", margin=dict(l=10, r=10, t=55, b=10))
    st.plotly_chart(fig, use_container_width=True)

    section_header("Flow View: How Friction Travels", "A simple Sankey view of how unclear inputs can create downstream delays.")
    labels = ["Unclear Inputs", "Different Formats", "Email-based Approvals", "Repeated Follow-ups", "Manual Reconciliation", "Delayed Closure", "Shared Tracker", "Standard Templates", "Faster Closure"]
    source = [0, 0, 2, 1, 3, 4, 6, 7]
    target = [1, 2, 3, 4, 4, 5, 8, 8]
    value = [5, 4, 4, 5, 4, 3, 4, 5]
    fig = go.Figure(data=[go.Sankey(
        node=dict(label=labels, pad=18, thickness=18),
        link=dict(source=source, target=target, value=value)
    )])
    fig.update_layout(title="From Friction to Progress Pathways", height=420, margin=dict(l=10, r=10, t=55, b=10))
    st.plotly_chart(fig, use_container_width=True)


def page_prioritization(filtered_df: pd.DataFrame):
    section_header("Impact × Feasibility Prioritization Matrix", "Identify quick wins and strategic projects respectfully.")
    if filtered_df.empty:
        st.warning("No records match the selected filters.")
        return
    df = filtered_df.copy()
    df["quadrant"] = df.apply(
        lambda r: "Quick Wins" if r["impact_score"] >= 4 and r["feasibility_score"] >= 4
        else "Strategic Projects" if r["impact_score"] >= 4 and r["feasibility_score"] < 4
        else "Monitor Later" if r["impact_score"] < 4 and r["feasibility_score"] >= 4
        else "Needs Leadership Support",
        axis=1,
    )
    fig = px.scatter(
        df,
        x="feasibility_score", y="impact_score",
        size="priority_score", color="quadrant",
        hover_name="constructive_reframe",
        hover_data=["category", "theme", "timeline", "suggested_kpi"],
        range_x=[0.5, 5.5], range_y=[0.5, 5.5],
        labels={"feasibility_score": "Feasibility", "impact_score": "Institutional Impact"},
        title="Discussion Matrix: What Should We Act on First?",
    )
    fig.add_vline(x=3.5, line_dash="dash", opacity=.4)
    fig.add_hline(y=3.5, line_dash="dash", opacity=.4)
    fig.update_layout(height=620, margin=dict(l=10, r=10, t=55, b=10))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### Quadrant Summary")
    summary = df.groupby("quadrant").agg(points=("constructive_reframe", "count"), avg_priority=("priority_score", "mean")).reset_index()
    summary["avg_priority"] = summary["avg_priority"].round(2)
    st.dataframe(summary, use_container_width=True, hide_index=True)


def page_top_bottlenecks():
    section_header("Top 3 Bottlenecks", "A concise synthesis for the retreat briefing.")
    for i, item in enumerate(TOP_BOTTLENECKS, 1):
        st.markdown(f"""
        <div class="card">
            <h3 style="color:{PRIMARY}; margin-bottom:.2rem;">{item['icon']} {i}. {item['title']}</h3>
            <p><strong>What we observed:</strong> {item['observed']}</p>
            <p><strong>Why it matters:</strong> {item['why_it_matters']}</p>
            <p><strong>Root cause:</strong> {item['root_cause']}</p>
            <p><strong>30–60 day quick win:</strong> {item['quick_win']}</p>
            <p><strong>Long-term institutional solution:</strong> {item['long_term']}</p>
            <span class="badge badge-teal">KPI: {item['kpi']}</span>
            <span class="badge badge-gold">Timeline: {item['timeline']}</span>
        </div>
        """, unsafe_allow_html=True)


def page_root_cause():
    section_header("Root Cause Analysis", "Interactive 5-Whys cards for the main bottlenecks.")
    five_whys = {
        "Delay in Data Consolidation": [
            "Inputs come in different formats.",
            "No common template is used across all submissions.",
            "SOPs are not uniformly followed or visible.",
            "Ownership and timelines are not always tracked centrally.",
            "There is no shared dashboard for submission status and pending actions.",
        ],
        "Repeated Approval Follow-ups": [
            "Approval status is sometimes embedded inside email threads.",
            "Stakeholders cannot always see whether an item is pending, approved, or queried.",
            "There is no common status language for approval closure.",
            "Responsibility for next action is not always visible.",
            "The process relies more on personal follow-up than system visibility.",
        ],
        "Last-Minute Workload Pressure": [
            "Requests may arrive close to deadlines.",
            "Urgency definitions are not always agreed in advance.",
            "Recurring tasks may not be mapped on a shared planning calendar.",
            "Teams handle urgent work while also managing planned work.",
            "TAT norms and escalation rules are not consistently institutionalized.",
        ],
    }
    selected = st.selectbox("Select root-cause card", list(five_whys.keys()))
    st.markdown(f"<div class='card'><h3 style='color:{PRIMARY};'>🔍 {selected}</h3></div>", unsafe_allow_html=True)
    for i, why in enumerate(five_whys[selected], 1):
        st.markdown(f"""
        <div class="soft-card" style="min-height:auto; margin-bottom:.55rem;">
            <span class="badge badge-blue">Why {i}</span> {why}
        </div>
        """, unsafe_allow_html=True)
    st.success("Root-cause synthesis: Standardized templates, visible ownership, common TATs, and shared tracking mechanisms can reduce avoidable friction without blaming any team.")


def page_solution_gallery():
    section_header("Solution Gallery", "Practical, realistic actions that can be adapted by teams.")
    solution_df = pd.DataFrame(SOLUTIONS)
    ease_filter = st.multiselect("Filter by ease", sorted(solution_df["ease"].unique()), default=sorted(solution_df["ease"].unique()))
    timeline_filter = st.multiselect("Filter by timeline", sorted(solution_df["timeline"].unique()), default=sorted(solution_df["timeline"].unique()))
    view = solution_df[solution_df["ease"].isin(ease_filter) & solution_df["timeline"].isin(timeline_filter)]
    cols = st.columns(3)
    for idx, row in view.iterrows():
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="progress-card">
                <div style="font-size:2.1rem;">{row['icon']}</div>
                <h4 style="color:{PRIMARY}; margin:.25rem 0;">{row['solution']}</h4>
                <p class="small-muted"><strong>Addresses:</strong> {row['problem']}</p>
                <span class="badge badge-teal">Ease: {row['ease']}</span>
                <span class="badge badge-gold">Impact: {row['impact']}</span>
                <p style="margin-top:.65rem;"><strong>Owner:</strong> {row['owner']}<br><strong>Timeline:</strong> {row['timeline']}<br><strong>KPI:</strong> {row['kpi']}</p>
            </div>
            """, unsafe_allow_html=True)


def page_roadmap():
    section_header("30–60–90 Day Roadmap", "Convert retreat insights into visible action.")
    cols = st.columns(3)
    colors = ["badge-blue", "badge-teal", "badge-gold"]
    icons = ["🚀", "🛠️", "📈"]
    for col, (stage, actions), color, icon in zip(cols, ROADMAP.items(), colors, icons):
        with col:
            st.markdown(f"<div class='progress-card'><h3 style='color:{PRIMARY};'>{icon} {stage}</h3>", unsafe_allow_html=True)
            for action in actions:
                st.markdown(f"<p>✅ {action}</p>", unsafe_allow_html=True)
            st.markdown(f"<span class='badge {color}'>Suggested review: end of {stage}</span></div>", unsafe_allow_html=True)

    st.markdown("#### Roadmap Progress Simulator")
    p30 = st.slider("First 30 Days completion", 0, 100, 25)
    p60 = st.slider("31–60 Days completion", 0, 100, 10)
    p90 = st.slider("61–90 Days completion", 0, 100, 0)
    st.progress((p30 + p60 + p90) / 300)
    st.caption(f"Overall indicative progress: {round((p30 + p60 + p90) / 3, 1)}%")


def page_kpi_tracker():
    section_header("KPI and Progress Tracker", "Use simple indicators to track whether friction is reducing.")
    if "kpis" not in st.session_state:
        st.session_state.kpis = DEFAULT_KPIS.copy()

    cols = st.columns(3)
    updated = {}
    for idx, (name, value) in enumerate(st.session_state.kpis.items()):
        with cols[idx % 3]:
            if "/ 5" in name:
                updated[name] = st.number_input(name, min_value=0.0, max_value=5.0, value=float(value), step=0.1)
            elif "%" in name:
                updated[name] = st.number_input(name, min_value=0, max_value=100, value=int(value), step=1)
            else:
                updated[name] = st.number_input(name, min_value=0, value=int(value), step=1)
    st.session_state.kpis = updated

    kpi_df = pd.DataFrame([{"KPI": k, "Current value": v} for k, v in updated.items()])
    st.dataframe(kpi_df, hide_index=True, use_container_width=True)
    fig = px.bar(kpi_df, x="Current value", y="KPI", orientation="h", title="Current KPI Values")
    fig.update_layout(height=520, margin=dict(l=10, r=10, t=55, b=10))
    st.plotly_chart(fig, use_container_width=True)


def page_reflection_wall():
    section_header("Interactive Reflection Wall", "Capture constructive ideas during discussion.")
    if "ideas" not in st.session_state:
        st.session_state.ideas = []

    prompts = [
        "One friction we can reduce",
        "One quick win we can implement",
        "One support needed from another team",
        "One practice we should standardize",
        "One idea for better collaboration",
    ]
    c1, c2 = st.columns([1, 1])
    with c1:
        prompt = st.selectbox("Reflection prompt", prompts)
        idea = st.text_area("Write a constructive idea", placeholder="Example: Create a common template for recurring data requests...")
        if st.button("Add to reflection wall", type="primary"):
            if idea.strip():
                st.session_state.ideas.append({"prompt": prompt, "text": idea.strip(), "time": datetime.now().strftime("%I:%M %p")})
                st.success("Idea added to the wall.")
            else:
                st.warning("Please write an idea before adding it.")
        if st.button("Clear reflection wall"):
            st.session_state.ideas = []
            st.info("Reflection wall cleared.")
    with c2:
        st.markdown("#### Live Ideas")
        if not st.session_state.ideas:
            st.info("No ideas added yet. Add the first constructive reflection.")
        else:
            for item in reversed(st.session_state.ideas):
                st.markdown(f"""
                <div class="sticky">
                    <span class="badge badge-blue">{item['prompt']}</span>
                    <p style="margin-top:.6rem;">{item['text']}</p>
                    <div class="small-muted">Added at {item['time']}</div>
                </div>
                """, unsafe_allow_html=True)


def page_report(filtered_df: pd.DataFrame):
    section_header("Downloadable Summary Report", "Export a concise action-oriented summary for follow-up.")
    report_md = make_report(filtered_df)
    st.download_button(
        "⬇️ Download Markdown Summary",
        data=report_md,
        file_name="fix_the_friction_summary.md",
        mime="text/markdown",
        type="primary",
    )
    st.download_button(
        "⬇️ Download Filtered Data CSV",
        data=filtered_df.to_csv(index=False).encode("utf-8"),
        file_name="fix_the_friction_filtered_data.csv",
        mime="text/csv",
    )
    with st.expander("Preview report"):
        st.markdown(report_md)


def page_presentation(filtered_df: pd.DataFrame):
    render_hero()
    st.write("")
    section_header("Executive Snapshot", "A presentation-first view for projector display.")
    c1, c2, c3 = st.columns(3)
    c1.metric("Improvement areas", filtered_df["category"].nunique() if not filtered_df.empty else 0)
    c2.metric("30-day candidates", int((filtered_df["timeline"] == "30 Days").sum()) if not filtered_df.empty else 0)
    c3.metric("Top synthesis themes", 3)

    section_header("Top 3 Bottlenecks", "Respectfully framed as system improvement opportunities.")
    for item in TOP_BOTTLENECKS:
        st.markdown(f"""
        <div class="card">
            <h2 style="color:{PRIMARY}; margin:.1rem 0;">{item['icon']} {item['title']}</h2>
            <p><strong>Quick win:</strong> {item['quick_win']}</p>
            <p><strong>KPI:</strong> {item['kpi']}</p>
        </div>
        """, unsafe_allow_html=True)

    section_header("30–60–90 Day Action Path", "From conversation to follow-through.")
    page_roadmap()

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.markdown("## 🧭 GIM Staff Retreat 2026")
    st.markdown("<span class='badge badge-teal'>Break the Barriers</span><br><span class='badge badge-gold'>Align · Collaborate · Deliver</span>", unsafe_allow_html=True)
    st.write("")
    presentation_mode = st.toggle("🎤 Presentation Mode", value=False)

    pages = [
        "Home",
        "Retreat Context",
        "Issue Explorer",
        "Visual Dashboard",
        "Prioritization Matrix",
        "Top 3 Bottlenecks",
        "Root Cause Analysis",
        "Solution Gallery",
        "30–60–90 Roadmap",
        "KPI Tracker",
        "Reflection Wall",
        "Download Report",
    ]
    if presentation_mode:
        page = "Presentation Mode"
        st.info("Presentation Mode is active. Controls are simplified for projector-friendly display.")
    else:
        page = st.radio("Navigate", pages, index=0)

FILTERED_DF = filter_data(DF) if not presentation_mode else DF.copy()

# ----------------------------
# Render pages
# ----------------------------
if presentation_mode:
    page_presentation(FILTERED_DF)
elif page == "Home":
    page_home(FILTERED_DF)
elif page == "Retreat Context":
    page_context()
elif page == "Issue Explorer":
    page_issue_explorer(FILTERED_DF)
elif page == "Visual Dashboard":
    page_visual_dashboard(FILTERED_DF)
elif page == "Prioritization Matrix":
    page_prioritization(FILTERED_DF)
elif page == "Top 3 Bottlenecks":
    page_top_bottlenecks()
elif page == "Root Cause Analysis":
    page_root_cause()
elif page == "Solution Gallery":
    page_solution_gallery()
elif page == "30–60–90 Roadmap":
    page_roadmap()
elif page == "KPI Tracker":
    page_kpi_tracker()
elif page == "Reflection Wall":
    page_reflection_wall()
elif page == "Download Report":
    page_report(FILTERED_DF)

st.markdown(
    """
    <div class="footer-note">
    Built for a constructive retreat discussion. All labels are intentionally framed as improvement opportunities, not complaints or personal assessments.
    </div>
    """,
    unsafe_allow_html=True,
)
