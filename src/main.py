"""
Dengue Prediction System - Desktop Edition
Run: python app.py
Requires: dengue_model.pkl at the path below
"""

import flet as ft
import joblib
import numpy as np

# ─────────────────────────────────────────────────────────────
#  COLOUR PALETTE
# ─────────────────────────────────────────────────────────────
BG         = "#F0F4F8"
SIDEBAR_BG = "#0B1F3A"
CARD_BG    = "#FFFFFF"
TEAL       = "#1B9E8F"
CORAL      = "#E5533C"
GOLD       = "#E8A838"
TEXT_DARK  = "#1A2332"
TEXT_MED   = "#4A5568"
TEXT_LIGHT = "#8A9AB0"
BORDER     = "#D8E2EE"
INPUT_BG   = "#F7FAFC"
TEAL_LIGHT = "#E6F6F4"
FEAT_CARD_BG = "#D9DBDE"



# ─────────────────────────────────────────────────────────────
#  LOAD MODEL  (unchanged from original)
# ─────────────────────────────────────────────────────────────
data     = joblib.load(r"C:/Users/AWOPETU/Desktop/IMPLEMENTATION/src/dengue_model.pkl")
model    = data["model"]
accuracy = 99.51 
 

# ─────────────────────────────────────────────────────────────
#  STYLED WIDGET HELPERS
# ─────────────────────────────────────────────────────────────
def make_tf(label: str, hint: str) -> ft.TextField:
    return ft.TextField(
        label=label,
        hint_text=hint,
        keyboard_type=ft.KeyboardType.NUMBER,
        bgcolor=INPUT_BG,
        border_color=BORDER,
        focused_border_color=TEAL,
        border_radius=8,
        label_style=ft.TextStyle(color=TEXT_MED, size=12, weight=ft.FontWeight.W_500),
        text_style=ft.TextStyle(color=TEXT_DARK, size=14),
        hint_style=ft.TextStyle(color=TEXT_LIGHT, size=12),
        content_padding=ft.padding.symmetric(horizontal=14, vertical=13),
        filled=True,
        cursor_color=TEAL,
        
    )
def card(content, padding=20):
    return ft.Container(
        content=content, bgcolor=CARD_BG,
        border_radius=20, padding=padding,
        
    )

def feat_card(icon, label, explanation):
    return ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Text(icon, size=14),
                border_radius=10,
                width=36, height=36,
                
            ),
            ft.Column([
                ft.Text(label, size=13, weight=ft.FontWeight.W_700, color=TEXT_MED),
                ft.Text(explanation, size=11, color=TEXT_MED),
            ], spacing=1, expand=True),
        ], spacing=12, vertical_alignment=ft.CrossAxisAlignment.CENTER),
        bgcolor=FEAT_CARD_BG,
        border_radius=12,
        padding=ft.padding.symmetric(horizontal=14, vertical=10),
        
    )

def make_fever(label: str) -> ft.Dropdown:
    ft.Dropdown(
        label = label,
        options=[ft.dropdown.Option("Yes"), ft.dropdown.Option("No")],
        value="No",
        bgcolor=INPUT_BG,
        border_color=BORDER,
        focused_border_color=TEAL,
        border_radius=8,
        label_style=ft.TextStyle(color=TEXT_MED, size=12, weight=ft.FontWeight.W_500),
        text_style=ft.TextStyle(color=TEXT_DARK, size=14),
        filled=True,
        content_padding=ft.padding.symmetric(horizontal=14, vertical=10), )

def make_dd(label: str) -> ft.Dropdown:
    return ft.Dropdown(
        label=label,
        options=[ft.dropdown.Option("Yes"), ft.dropdown.Option("No")],
        value="No",
        bgcolor=INPUT_BG,
        border_color=BORDER,
        focused_border_color=TEAL,
        border_radius=8,
        label_style=ft.TextStyle(color=TEXT_MED, size=12, weight=ft.FontWeight.W_500),
        text_style=ft.TextStyle(color=TEXT_DARK, size=14),
        filled=True,
        content_padding=ft.padding.symmetric(horizontal=14, vertical=10),
    )


def section_label(text: str, icon: str) -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Text(icon, size=13),
                bgcolor=TEAL_LIGHT,
                border_radius=6,
                padding=ft.padding.all(6),
            ),
            ft.Text(text, size=11, weight=ft.FontWeight.W_700,
                    color=TEXT_MED),  
        ], spacing=10),
        margin=ft.margin.only(bottom=10, top=6),
    )


def row2(a, b) -> ft.Row:
    """Two controls side-by-side, equal width."""
    return ft.Row([
        ft.Container(content=a, expand=True),
        ft.Container(content=b, expand=True),
    ], spacing=14)


def feat_row(icon, label) -> ft.Container:
    return ft.Container(
        content=ft.Row([
            ft.Text(icon, size=14),
            ft.Text(label, size=12, color=TEXT_MED),
        ], spacing=10),
        bgcolor=TEAL_LIGHT,
        border_radius=8,
        padding=ft.padding.symmetric(horizontal=12, vertical=8),
    )


def stat_row(icon, label) -> ft.Row:
    return ft.Row([
        ft.Text(icon, size=15),
        ft.Text(label, size=13, color="#9FBDD8"),
    ], spacing=12)


# ─────────────────────────────────────────────────────────────
#  LANDING SCREEN
# ─────────────────────────────────────────────────────────────
def build_landing(page: ft.Page, on_begin):
    name_field = ft.TextField(
        hint_text="Your full name…",
        bgcolor=INPUT_BG,
        border_color=BORDER,
        focused_border_color=TEAL,
        border_radius=10,
        text_style=ft.TextStyle(color=TEXT_DARK, size=15),
        hint_style=ft.TextStyle(color=TEXT_LIGHT),
        content_padding=ft.padding.symmetric(horizontal=18, vertical=16),
        filled=True,
        cursor_color=TEAL,
        on_submit=lambda e: try_begin(e),
    )
    err = ft.Text("Please enter your name to continue.",
                  color=CORAL, size=12, visible=False)

    def try_begin(e):
        name = name_field.value.strip()
        if not name:
            name_field.border_color = CORAL
            err.visible = True
            page.update()
            return
        err.visible = False
        on_begin(name)

    left = ft.Container(
        content=ft.Column([
            ft.Text("🦟", size=64),
            ft.Container(height=20),
            ft.Text("Dengue\nPrediction\nSystem",
                    size=38, weight=ft.FontWeight.W_900,
                    color=ft.Colors.WHITE ),  #line_spacing=4
            ft.Container(height=16),
            ft.Text("Machine Learning-based prediction system for dengue fever.",
                    size=14, color="#7A9CC0"), # line_spacing=6
            ft.Container(height=40),
            ft.Column([
                stat_row("🔬", "Lab-value analysis"),
                stat_row("📊", "Random Forest model"),
                stat_row("⚡", "Instant results"),
            ], spacing=14),
        ], spacing=0),
        bgcolor=SIDEBAR_BG,
        expand=2,
        padding=ft.padding.symmetric(horizontal=56, vertical=64),
    )

    right = ft.Container(
        content=ft.Column([
            ft.Container(expand=True),
            ft.Text("Welcome", size=30, weight=ft.FontWeight.W_800, color=TEXT_DARK),
            ft.Container(height=6),
            ft.Text("Enter your name to begin the assessment.",
                    size=14, color=TEXT_MED),
            ft.Container(height=36),
            ft.Text("YOUR NAME", size=11, weight=ft.FontWeight.W_700,
                    color=TEXT_MED), #letter_spacing=1.4
            ft.Container(height=8),
            name_field,
            err,
            ft.Container(height=20),
            ft.ElevatedButton(
                content=ft.Row([
                    ft.Text("BEGIN ASSESSMENT", size=13,
                            weight=ft.FontWeight.W_700, color=ft.Colors.WHITE),
                    ft.Icon(ft.Icons.ARROW_FORWARD_ROUNDED, size=16,
                            color=ft.Colors.WHITE),
                ], spacing=10, alignment=ft.MainAxisAlignment.CENTER),
                bgcolor=TEAL,
                width=9999,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=10),
                    padding=ft.padding.symmetric(vertical=18),
                    elevation=0,
                ),
                on_click=try_begin,
            ),
            ft.Container(height=24),
            ft.Text(
                "⚕️  For informational use only. Not a substitute for medical advice.",
                size=11, color=TEXT_LIGHT, text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(expand=True),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        expand=3,
        padding=ft.padding.symmetric(horizontal=72, vertical=40),
        bgcolor=BG,
    )

    return ft.Row([left, right], expand=True, spacing=0)


# ─────────────────────────────────────────────────────────────
#  DIAGNOSIS SCREEN
# ─────────────────────────────────────────────────────────────
def build_diagnosis(page: ft.Page, username: str):

    accuracy_badge = ft.Container(
        content=ft.Row([
            ft.Text(
                f"{accuracy}% accuracy",
                size=11,
                weight=ft.FontWeight.W_500,
                color="#393A3E",
            ),
        ], spacing=4, tight=True),
        # bgcolor="#001A26",
        border_radius=8,
        padding=ft.padding.symmetric(horizontal=12, vertical=5),
        border=ft.border.all(0.8, "#003344"),
    )

    # ── Input fields (same names/labels as original) ──────────
    wbc      = make_tf("WBC", "e.g. 5000")
    platelet = make_tf("Platelet Count", "e.g. 150000")
    duration = make_tf("Duration of Fever (days)", "e.g. 5")
    muscle   = make_dd("Muscle Pain")
    headache = make_dd("Headache")
    vomiting = make_dd("Vomiting")
    rash     = make_dd("Rash")

    # ── Fever → duration linkage ──────────────────────────────
    # When Fever is set to "No", duration is cleared, forced to "0",
    # and made read-only so the user cannot enter a value > 0.
    def on_fever_change(e):
        if fever.value == "No":
            duration.value      = "0"
            duration.read_only  = True
            duration.bgcolor    = "#EEEEEE"
            duration.hint_text  = "N/A — no fever"
            duration.error = None
        else:
            duration.value      = ""
            duration.read_only  = False
            duration.bgcolor    = INPUT_BG
            duration.hint_text  = "e.g. 5"
        page.update()
 
    fever = ft.Dropdown(
        label="Fever",
        options=[ft.dropdown.Option("Yes"), ft.dropdown.Option("No")],
        value="No",
        on_text_change=on_fever_change,
        bgcolor=INPUT_BG,
        border_color=BORDER,
        focused_border_color=TEAL,
        border_radius=8,
        label_style=ft.TextStyle(color=TEXT_MED, size=12, weight=ft.FontWeight.W_500),
        text_style=ft.TextStyle(color=TEXT_DARK, size=14),
        filled=True,
        content_padding=ft.padding.symmetric(horizontal=14, vertical=10),
    )

    # Initialise duration as locked because fever defaults to "No"
    duration.value     = "0"
    duration.read_only = True
    duration.bgcolor   = "#EEEEEE"
    duration.hint_text = "N/A — no fever"

    # ── Result display widgets ────────────────────────────────
    result_text = ft.Text("", size=17, weight=ft.FontWeight.BOLD,
                          text_align=ft.TextAlign.CENTER)
    progress    = ft.ProgressRing(visible=False, color=TEAL,
                                  stroke_width=3, width=30, height=29)

    # ── Validation (unchanged logic from original) ────────────
    def validate():
        valid = True
        for field in [wbc, platelet, duration]:
            field.error = None

        try:
            if float(wbc.value) <= 0:
                wbc.error = "Enter valid WBC"
                valid = False
        except Exception:
            wbc.error = "Enter valid WBC"
            valid = False

        try:
            if float(platelet.value) <= 0:
                platelet.error = "Enter valid platelet count"
                valid = False
        except Exception:
            platelet.error = "Enter valid platelet count"
            valid = False

        try:
            dur_val = float(duration.value)
            # Duration must be > 0 when fever is present;
            # it is locked to 0 automatically when fever is "No" — that is valid.
            if fever.value == "Yes" and dur_val <= 0:
                duration.error = "Enter valid duration (must be > 0 when fever is present)"
                valid = False
        except Exception:
            duration.error = "Enter valid duration"
            valid = False

        return valid
    # def validate() -> bool:
    #     ok = True

    #     def chk(field, err, msg, lo=0, hi=1e9):
    #         nonlocal ok
    #         try:
    #             v = float(field.value)
    #             if not (lo < v <= hi):
    #                 raise ValueError
    #             field.border_color = BORDER
    #             err.visible = False
    #         except Exception:
    #             field.border_color = CORAL
    #             err.value = msg
    #             err.visible = True
    #             ok = False

    #     chk(wbc,      wbc_err,      "Enter a valid WBC count (> 0)")
    #     chk(platelet, platelet_err, "Enter a valid platelet count (> 0)")
    #     chk(duration, duration_err, "Enter fever duration in days (1–30)", lo=0, hi=31)
    #     return ok
    # ── Prediction (unchanged logic from original) ────────────
    def predict(e):
        if not validate():
            page.update()
            return

        progress.visible = True
        result_text.value = "Analyzing..."
        page.update()

        input_data = np.array([[
            float(wbc.value),
            float(platelet.value),
            1 if muscle.value == "Yes" else 0,
            1 if fever.value == "Yes" else 0,
            1 if headache.value == "Yes" else 0,
            float(duration.value),
            1 if vomiting.value == "Yes" else 0,
            1 if rash.value == "Yes" else 0
        ]])

        prediction = model.predict(input_data)[0]

        try:
            prob = model.predict_proba(input_data)[0][1] * 100
        except Exception:
            prob = 0

        if prob > 70:
            risk  = " High Risk"
            color = "red"
        elif prob > 40:
            risk  = " Moderate Risk"
            color = "orange"
        else:
            risk  = " Low Risk"
            color = "green"

        if prediction == 1:
            result_text.value = f"{risk}\n⚠️ Dengue Detected ({prob:.2f}%)"
        else:
            result_text.value = f"{risk}\n✅ No Dengue ({100 - prob:.2f}%)"

        result_text.color   = color
        progress.visible    = False
        page.update()

    # ── Reset (unchanged logic from original) ─────────────────
    def reset(e):
        wbc.value      = ""
        platelet.value = ""
        muscle.value   = "No"
        fever.value    = "No"
        headache.value = "No"
        vomiting.value = "No"
        rash.value     = "No"
        result_text.value = ""
        for f in [wbc, platelet, duration]:
            f.error = None
        # Re-lock duration because fever resets to "No"
        duration.value     = "0"
        duration.read_only = True
        duration.bgcolor   = "#EEEEEE"
        duration.hint_text = "N/A — no fever"
        page.update()

    # ─── LEFT: form ───────────────────────────────────────────
    form = ft.Container(
        content=ft.Column([

            # Header row
            ft.Container(
                content=ft.Row([
                    ft.Column([
                        ft.Text(f"Welcome, {username}", size=13, color=TEXT_MED),
                        ft.Text("Dengue Risk Assessment",
                                size=22, weight=ft.FontWeight.W_800, color=TEXT_DARK),
                        accuracy_badge,
                    ], spacing=2),
                    ft.Container(expand=True),
                    ft.TextButton(
                        content=ft.Row([
                            ft.Icon(ft.Icons.REFRESH_ROUNDED, size=16, color=TEXT_MED),
                            ft.Text("Reset", size=13, color=TEXT_MED),
                        ], spacing=6),
                        on_click=reset,
                    ),
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                   vertical_alignment=ft.CrossAxisAlignment.CENTER),
                padding=ft.padding.only(bottom=20),
            ),

            ft.Divider(height=1, color=BORDER),
            ft.Container(height=12),

            # Lab values
            section_label("LABORATORY VALUES", "🔬"),
            row2(wbc, platelet),
            ft.Container(height=10),

            # Symptoms
            section_label("CLINICAL SYMPTOMS", "🩺"),
            row2(muscle, headache),
            ft.Container(height=10),
            row2(vomiting, rash),
            ft.Container(height=10),

            # Fever details — fever dropdown LEFT, duration field RIGHT
            section_label("FEVER DETAILS", "🌡️"),
            row2(fever, duration),
            ft.Container(height=24),

            # Action buttons
            ft.Row([
                ft.OutlinedButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.REFRESH_ROUNDED, size=15, color=TEXT_MED),
                        ft.Text("Reset", size=13, color=TEXT_MED),
                    ], spacing=6),
                    style=ft.ButtonStyle(
                        side=ft.BorderSide(1, BORDER),
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(vertical=15, horizontal=20),
                    ),
                    on_click=reset,
                ),
                ft.ElevatedButton(
                    content=ft.Row([
                        ft.Icon(ft.Icons.ANALYTICS_ROUNDED, size=16,
                                color=ft.Colors.WHITE),
                        ft.Text("PREDICT", size=13, weight=ft.FontWeight.W_700,
                                color=ft.Colors.WHITE),
                    ], spacing=8, alignment=ft.MainAxisAlignment.CENTER),
                    bgcolor=TEAL,
                    expand=True,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=8),
                        padding=ft.padding.symmetric(vertical=15),
                        elevation=0,
                    ),
                    on_click=predict,
                ),
            ], spacing=12),

        ], spacing=0, scroll=ft.ScrollMode.AUTO),
        expand=3,
        bgcolor=CARD_BG,
        padding=ft.padding.symmetric(horizontal=36, vertical=32),
    )

    # ─── RIGHT: result sidebar ────────────────────────────────
    sidebar = ft.Container(
        content=ft.Column([

            # Branding strip
            ft.Container(
                content=ft.Column([
                    ft.Text("🦟", size=32),
                    ft.Container(height=4),
                    ft.Text("Dengue\nPrediction\nSystem",
                            size=18, weight=ft.FontWeight.W_900,
                            color=ft.Colors.WHITE, # line_spacing=2,
                            text_align=ft.TextAlign.CENTER),
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
                bgcolor=SIDEBAR_BG,
                padding=ft.padding.symmetric(vertical=28, horizontal=16),
                border_radius=ft.border_radius.only(top_right=16),
                width=9999,
            ),

            ft.Container(height=20),

            # Result card
            ft.Container(
                content=ft.Column([
                    ft.Text("RESULT", size=10, weight=ft.FontWeight.W_700,
                            color=TEXT_LIGHT), #letter_spacing=1.4
                    ft.Container(height=14),
                    ft.Row([progress],
                           alignment=ft.MainAxisAlignment.CENTER),
                    result_text,
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
                bgcolor=CARD_BG,
                border_radius=12,
                padding=ft.padding.symmetric(horizontal=18, vertical=22),
                border=ft.border.all(1, BORDER),
                shadow=ft.BoxShadow(blur_radius=12, color="#0000001A",
                                    offset=ft.Offset(0, 3)),
                margin=ft.margin.symmetric(horizontal=16),
            ),

            ft.Container(height=18),

            # Key features card
            # ft.Container(
            #     content=ft.Column([
            #         ft.Text("KEY FEATURES", size=10, weight=ft.FontWeight.W_700,
            #                 color=TEXT_LIGHT), #letter_spacing=1.4
            #         ft.Container(height=10),
            #         *[feat_row(ic, lb) for ic, lb in [
            #             ("🩸", "Platelet Count"),
            #             ("🔬", "WBC Count"),
            #             ("🌡️", "Fever Duration"),
            #             ("💢", "Skin Rash"),
            #             ("🤕", "Headache"),
            #         ]],
            #     ], spacing=8),
            #     bgcolor=CARD_BG,
            #     border_radius=12,
            #     padding=ft.padding.symmetric(horizontal=18, vertical=18),
            #     border=ft.border.all(1, BORDER),
            #     margin=ft.margin.symmetric(horizontal=16),
            # ),
            
            card(ft.Column([
                    ft.Text("KEY FEATURES", size=10, weight=ft.FontWeight.W_700,
                            color=TEXT_LIGHT), #letter_spacing=1.4),
                    ft.Container(height=12),
                    feat_card("🩸", "Platelet Count",
                              "Number of platelets per microliter of blood."),
                    ft.Container(height=8),
                    feat_card("🔬", "WBC Count",
                              "Number of white blood cells per microliter of blood."),
                    ft.Container(height=8),
                    feat_card("💢", "Skin Rash",
                              "Presence of a red rash on the skin."),
                    ft.Container(height=8),
                    feat_card("🤕", "Headache",
                              "Presence of pain in the head or behind the eyes."),
                ], spacing=0), padding=18),

                ft.Container(height=30),

            ft.Container(expand=True),

            # Disclaimer
            ft.Container(
                content=ft.Text(
                    "⚕️  For informational use only. \nNot a substitute for medical advice.",
                    size=11, color=TEXT_LIGHT, text_align=ft.TextAlign.CENTER,
                ),
                padding=ft.padding.symmetric(horizontal=16, vertical=14),
            ),

        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=0),
        expand=2,
        bgcolor=BG,
        border_radius=ft.border_radius.only(top_right=16, bottom_right=16),
        border=ft.border.only(left=ft.BorderSide(1, BORDER)),
    )

    return ft.Row([form, sidebar], expand=True, spacing=0)


# ─────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────
def main(page: ft.Page):
    page.title = "Dengue Prediction System"
    page.bgcolor = BG
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.window.width    = 960
    page.window.height   = 680
    page.window.min_width  = 780
    page.window.min_height = 560
    page.window.resizable  = True

    def go_to_diagnosis(name: str):
        page.controls.clear()
        page.add(
            ft.Container(
                content=build_diagnosis(page, name),
                expand=True,
                border_radius=16,
                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                shadow=ft.BoxShadow(blur_radius=40, color="#00000018",
                                    offset=ft.Offset(0, 8)),
                margin=ft.margin.all(24),
            )
        )
        page.update()

    page.add(
        ft.Container(
            content=build_landing(page, go_to_diagnosis),
            expand=True,
            border_radius=16,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(blur_radius=40, color="#00000018",
                                offset=ft.Offset(0, 8)),
            margin=ft.margin.all(24),
        )
    )
    page.update()


ft.run(main)