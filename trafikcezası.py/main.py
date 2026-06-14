import flet as ft

# Güvenli hizalama bloğu
try:
    _align_top_left = ft.Alignment.TOP_LEFT
    _align_bottom_right = ft.Alignment.BOTTOM_RIGHT
    _align_center = ft.Alignment.CENTER
except AttributeError:
    _align_top_left = ft.alignment.top_left
    _align_bottom_right = ft.alignment.bottom_right
    _align_center = ft.alignment.center

def main(page: ft.Page):
    page.title = "Canım Babam - Babalar Günü Kutlu Olsun"
    page.padding = 0
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.DARK 

    # --- 1. KOYU LACİVERT ÜST ÇUBUK (APPBAR) ---
    page.appbar = ft.AppBar(
        leading=ft.Container(
            content=ft.Text("❤️", size=26), 
            padding=ft.Padding(left=15, top=0, right=0, bottom=0), 
            alignment=_align_center
        ),
        leading_width=60,
        title=ft.Text(
            "BABALAR GÜNÜN KUTLU OLSUN CANIM BABAM", 
            weight="bold", 
            size=20, 
            color="#000000", 
            font_family="System-UI"
        ),
        center_title=True,
        bgcolor="#0d1b2a", # Koyu lacivert
        elevation=3,
    )

    # --- 2. SÜRPRİZ AÇILIR PENCERE (DIALOG) ---
    def dialog_kapat(e):
        surpriz_dialog.open = False
        page.update()

    surpriz_dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("Sürpriiiz! 💌", text_align="center", size=24, weight="bold", color="#000000"),
        content=ft.Text(
            "İyi ki varsın canım babam, iyi ki hayatımızdasın.",
            size=20,
            weight="bold",
            text_align="center",
            color="#000000" 
        ),
        bgcolor="#1b263b", # Koyu lacivert
        actions=[
            ft.TextButton(
                content=ft.Text("Kapat ❌", size=16, color="#ef4444", weight="bold"), 
                on_click=dialog_kapat
            )
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER
    )
    
    page.overlay.append(surpriz_dialog)

    def surpriz_ac(e):
        surpriz_dialog.open = True
        page.update()

    surpriz_butonu = ft.ElevatedButton(
        content=ft.Text("Mesajı Okumak İçin Tıkla 💌", size=22, weight="bold", color="#000000"),
        on_click=surpriz_ac,
        style=ft.ButtonStyle(
            bgcolor="#415a77",
            padding=30, 
            shape=ft.RoundedRectangleBorder(radius=15),
            elevation=10
        )
    )

    # --- 3. ANİMASYONLU FOTOĞRAF OLUŞTURUCU ---
    def hover_efekti(e):
        e.control.scale = 1.1 if e.data == "true" else 1.0
        e.control.update()

    def foto_olustur(dosya_adi, w=350, h=500):
        return ft.Container(
            content=ft.Image(
                src=dosya_adi, 
                width=w,
                height=h,
                fit="cover",
                border_radius=10 
            ),
            bgcolor="#1b263b", # Koyu lacivert
            padding=6,  
            border_radius=16,
            scale=1.0,
            animate_scale=300, 
            on_hover=hover_efekti,
        )

    # MODERN YAZI OLUŞTURUCU 
    def yazi_olustur(metin, boyut=45):
        return ft.Container(
            content=ft.Text(
                value=metin,
                size=boyut,
                weight="bold", 
                color="#000000", # Siyah yazı
                text_align="center", 
                font_family="Segoe UI" 
            ),
            bgcolor="#1b263b", # Koyu lacivert
            padding=30, 
            border_radius=20,
            expand=True,
            alignment=_align_center,
            margin=20 
        )

    # SEKMELERİ OLUŞTURAN FONKSİYON 
    def sekme_olustur(resim_sol, metin, resim_sag, is_multi=False):
        if not is_multi:
            sol_content = foto_olustur(resim_sol)
            sag_content = foto_olustur(resim_sag)
        else:
            sol_content = ft.Column([
                foto_olustur(resim_sol[0], 280, 350), 
                foto_olustur(resim_sol[1], 280, 350)
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER) 
            
            sag_content = ft.Column([
                foto_olustur(resim_sag[0], 280, 350), 
                foto_olustur(resim_sag[1], 280, 350)
            ], spacing=20, alignment=ft.MainAxisAlignment.CENTER)

        return ft.Container(
            content=ft.Row(
                controls=[
                    sol_content,
                    yazi_olustur(metin),
                    sag_content
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND, 
                vertical_alignment=ft.CrossAxisAlignment.CENTER, 
            ),
            padding=40, 
            height=850 
        )

    # --- İÇERİK AKIŞI (TAM 10 FOTOĞRAF) ---
    
    # 1. Sayfa (2 Fotoğraf)
    sekme_1 = sekme_olustur(
        "sol1.jpg", 
        "BABALAR GÜNÜN\nKUTLU OLSUN\nCANIM BABAM", 
        "sag1.jpg"
    )

    # 2. Sayfa (4 Fotoğraf)
    sekme_2 = sekme_olustur(
        ["s2_sol_ust.jpg", "s2_sol_alt.jpg"], 
        "BABALAR GÜNÜN\nKUTLU OLSUN\nCANIM BABAM", 
        ["s2_sag_ust.jpg", "s2_sag_alt.jpg"], 
        is_multi=True
    )

    # 3. Sayfa (4 Fotoğraf)
    sekme_3 = sekme_olustur(
        ["s3_sol_ust.jpg", "s3_sol_alt.jpg"], 
        "BABALAR GÜNÜN\nKUTLU OLSUN\nCANIM BABAM", 
        ["s3_sag_ust.jpg", "s3_sag_alt.jpg"], 
        is_multi=True
    )

    # ANA TAŞIYICI 
    ana_arkaplan = ft.Container(
        content=ft.Column(
            controls=[
                sekme_1, 
                sekme_2, 
                sekme_3, 
                ft.Container(
                    content=ft.Row([surpriz_butonu], alignment=ft.MainAxisAlignment.CENTER),
                    padding=50 
                )
            ],
            spacing=50,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        bgcolor="#0d1b2a", # Ana arka plan tamamen koyu lacivert
        padding=40, 
        expand=True
    )

    page.add(ana_arkaplan)

# Dosya yolu assets olarak düzeltildi
ft.app(target=main, assets_dir="assets")