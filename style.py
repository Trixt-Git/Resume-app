STYLE = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,500&display=swap');

:root {
  --bg: #F7F8F5;
  --surface: #FFFFFF;
  --ink: #17251B;
  --muted: #5C6B61;
  --line: #DCE5DB;

  /* Fidelity-green palette (matches .streamlit/config.toml primaryColor) */
  --green: #3F7623;
  --green-dark: #2D5519;
  --green-soft: #EEF4EC;

  --gold: #A46F18;
  --gold-soft: #FBF4E3;
}


/* Page */
html, body, [data-testid="stAppViewContainer"] {
  background-color: var(--bg);
  color: var(--ink);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* The top chrome (Deploy button, menu) is disabled via client.toolbarMode in
   config.toml; this just collapses the now-empty header bar's reserved space. */
[data-testid="stHeader"] {
  height: 2.5rem;
  background: transparent;
}


/* Layout */
.block-container {
  max-width: 700px;
  padding-top: 1.5rem;
  padding-bottom: 2rem;
}


/* Sidebar navigation */
[data-testid="stSidebar"] {
  background: var(--surface);
  border-right: 1px solid var(--line);
}

[data-testid="stSidebarNavLink"] {
  border-radius: 8px;
  color: var(--muted) !important;
  font-weight: 500;
}

[data-testid="stSidebarNavLink"]:hover {
  background: var(--green-soft) !important;
}

[data-testid="stSidebarNavLink"][aria-current="page"] {
  background: var(--green-soft) !important;
  color: var(--green-dark) !important;
  font-weight: 700;
}


/* WilOS branding */
.wilos-title {
  font-family: 'Fraunces', Georgia, serif;
  font-size: 2.6rem;
  font-weight: 500;
  letter-spacing: -0.06em;
  line-height: 1;
  color: var(--ink);
  margin-bottom: 0.4rem;
}

.wilos-title span {
  font-size: 1.25em;
  font-weight: 700;
  color: var(--green);
  letter-spacing: -0.05em;
}

.wilos-subtitle {
  color: var(--muted);
  font-size: 1rem;
  line-height: 1.6;
  max-width: 600px;
  margin-bottom: 2rem;
}


/* Headers */
h1, h2 {
  font-family: 'Fraunces', Georgia, serif;
  font-weight: 500;
  color: var(--green-dark);
}

/* The "WilOS" page title in chat mode — tighter than Streamlit's default
   heading margins so the conversation panel starts right under it. */
[data-testid="stHeading"] h1 {
  margin: 0 0 1rem;
}


/* Text */
.stMarkdown p {
  color: var(--muted);
  line-height: 1.65;
}


/* Chat panel: gives the transcript a defined boundary instead of loose
   bubbles floating on the page background. */
.st-key-wilos_chat_panel {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 16px;
  padding: 1.25rem 1.25rem 0.25rem;
}

.st-key-wilos_chat_panel [data-testid="stChatMessage"]:last-child {
  margin-bottom: 0;
}

/* Chat cards */
[data-testid="stChatMessage"] {
  background: var(--bg);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 1rem 1.2rem;
  margin-bottom: 0.9rem;
}


/* Wil label */
.askwil-label {
  font-size: 0.7rem;
  font-weight: 700;
  color: var(--green);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  margin-bottom: 0.5rem;
}


/* Citation markers */
.askwil-marker {
  margin-top: 0.8rem;
  padding: 0.5rem 0.8rem;
  border-left: 3px solid var(--line);
  border-radius: 6px;
  font-size: 0.78rem;
  line-height: 1.4;
}


.askwil-marker--source {
  border-left-color: var(--green);
  background: var(--green-soft);
  color: var(--muted);
}


.askwil-marker--refusal {
  border-left-color: var(--gold);
  background: var(--gold-soft);
  color: var(--gold);
  font-weight: 600;
}


/* Prompt buttons */
.stButton button {
  width: 100%;
  min-height: 46px;
  border-radius: 12px !important;
  border: 1px solid var(--line) !important;
  background: var(--surface) !important;
  color: var(--green-dark) !important;
  font-weight: 600;
  transition: all 0.15s ease;
}


.stButton button:hover {
  background: var(--green-soft) !important;
  border-color: var(--green) !important;
}


/* Chat input */
[data-testid="stChatInput"] {
  border-radius: 14px;
}


/* Focus accessibility */
.stButton button:focus-visible,
textarea:focus-visible,
input:focus-visible {
  outline: 2px solid var(--green) !important;
  outline-offset: 2px;
}


/* Optional timeline / flow components */
.wilos-flow {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin: 1.5rem 0;
}


.wilos-flow-step {
  background: var(--surface);
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 0.9rem 1rem;
}


.wilos-flow-arrow {
  text-align: center;
  color: var(--muted);
}


/* Quick-action pill row, shared by the empty-state hero and the persistent
   bottom bar — same column/button treatment in both places. */
.st-key-wilos_hero [data-testid="stHorizontalBlock"],
.st-key-wilos_bottom [data-testid="stHorizontalBlock"] {
  justify-content: center !important;
  gap: 0.5rem !important;
  flex-wrap: wrap !important;
  width: auto !important;
}

.st-key-wilos_bottom [data-testid="stHorizontalBlock"] {
  margin: 0.6rem auto 0 !important;
}

.st-key-wilos_hero [data-testid="stColumn"],
.st-key-wilos_bottom [data-testid="stColumn"] {
  width: fit-content !important;
  flex: 0 0 auto !important;
  min-width: 0 !important;
}

.st-key-wilos_hero .stButton button,
.st-key-wilos_bottom .stButton button {
  width: auto !important;
  padding-left: 1.1rem;
  padding-right: 1.1rem;
}


/* Centered landing hero (empty-state only) */
.st-key-wilos_hero {
  display: flex !important;
  flex-direction: column !important;
  justify-content: center !important;
  align-items: center !important;
  min-height: 35vh !important;
  text-align: center !important;
}

.st-key-wilos_hero [data-testid="stMarkdownContainer"],
.st-key-wilos_hero [data-testid="stMarkdownContainer"] p {
  text-align: center !important;
}

.st-key-wilos_hero [data-testid="stChatInput"] {
  width: 100% !important;
  margin: 1.5rem 0 1.25rem !important;
}


/* Mobile */
@media (max-width: 640px) {

  .block-container {
    padding-left: 1rem;
    padding-right: 1rem;
  }

  .wilos-title {
    font-size: 2.1rem;
  }

}


/* Accessibility: respect reduced-motion preference */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}

</style>
"""
