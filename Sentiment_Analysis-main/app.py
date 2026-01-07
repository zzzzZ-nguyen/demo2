import streamlit as st

# ==========================
# ⚙️ CẤU HÌNH TRANG
# ==========================
st.set_page_config(
    page_title="Topic 5 – Sentiment Analysis for E-Commerce",
    page_icon="https://cdn-icons-png.flaticon.com/512/3143/3143636.png",
    layout="wide"
)

# ==========================
# 🖌️ CUSTOM CSS (LÀM ĐẸP GIAO DIỆN)
# ==========================
# Tại đây mình thêm hình nền pattern nhẹ và chỉnh lại font/màu sắc
st.markdown(
    """
    <style>
    /* 1. Thay đổi hình nền chính */
    [data-testid="stAppViewContainer"] {
        background-color: #f8f9fa;
        background-image: radial-gradient(#e3e8eb 1px, transparent 1px), radial-gradient(#e3e8eb 1px, #f8f9fa 1px);
        background-size: 20px 20px;
        background-position: 0 0, 10px 10px;
    }

    /* 2. Chỉnh sửa Sidebar */
    [data-testid="stSidebar"] {
        background-image: linear-gradient(180deg, #e0f7fa 0%, #ffffff 100%);
        border-right: 1px solid #dcdcdc;
    }

    /* 3. Hiệu ứng tiêu đề */
    h2 {
        background: -webkit-linear-gradient(45deg, #1b5e20, #4caf50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* 4. Style cho các box thông tin (Glassmorphism) */
    .info-box {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.3);
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    .info-box:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# 🎨 HEADER
# ==========================
col1, col2 = st.columns([1, 9])

with col1:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/10605/10605943.png", # Icon 3D đẹp hơn
        width=85
    )

with col2:
    st.markdown(
        """
        <div style="padding-top: 10px;">
            <h2 style="margin-bottom:0; font-family: 'Segoe UI', sans-serif;">
                Topic 5: Developing a Sentiment Analysis Application
            </h2>
            <h4 style="color:#555; margin-top:5px; font-weight: 400;">
                Supporting E-Commerce Business Decision Making 🚀
            </h4>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("---")

# ==========================
# 📌 SIDEBAR – NAVIGATION
# ==========================
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/9187/9187604.png", width=50)
st.sidebar.markdown("## 🧭 **Navigation**")

page = st.sidebar.radio(
    "",
    [
        "Home – Giới thiệu đề tài",
        "Analysis – Sentiment Analysis",
        "Training Info – Thông tin mô hình"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Note:** Select a page above to navigate.")

# ==========================
# 📦 ROUTING
# ==========================
# (Giữ nguyên logic của bạn, chỉ thêm try-except để tránh lỗi nếu chưa có file pages)
try:
    if page == "Home – Giới thiệu đề tài":
        from pages.Home import show
        show()

    elif page == "Analysis – Sentiment Analysis":
        from pages.Analysis import show
        show()

    elif page == "Training Info – Thông tin mô hình":
        from pages.Training_Info import show
        show()
except ImportError:
    st.error("⚠️ Không tìm thấy file trong thư mục 'pages'. Vui lòng kiểm tra lại cấu trúc thư mục.")
except Exception as e:
    st.error(f"Đã xảy ra lỗi: {e}")

# ==========================
# 👣 FOOTER (NÂNG CẤP GIAO DIỆN)
# ==========================
st.markdown("---")
st.markdown("<br>", unsafe_allow_html=True)

# -------- STUDENTS BOX (NÂNG CẤP) --------
st.markdown(
    """
    <div class="info-box" style="border-left: 5px solid #fbc02d;">
        <h5 style="color: #f57f17; margin-bottom: 10px;">🎓 Students Implementation</h5>
        <div style="display: flex; gap: 20px; flex-wrap: wrap;">
            <div>
                <b>👤 Bui Duc Nguyen</b><br>
                <span style="color:#666; font-size:14px;">ID: 235053154</span><br>
                <a href="mailto:nguyenbd23@uef.edu.vn" style="text-decoration:none; color:#1976d2; font-size:13px;">📧 nguyenbd23@uef.edu.vn</a>
            </div>
            <div style="border-left: 1px solid #ddd; padding-left: 20px;">
                <b>👤 Huynh Ngoc Minh Quan</b><br>
                <span style="color:#666; font-size:14px;">ID: 235052863</span><br>
                <a href="mailto:quanhnm@uef.edu.vn" style="text-decoration:none; color:#1976d2; font-size:13px;">📧 quanhnm@uef.edu.vn</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------- INSTRUCTOR BOX (NÂNG CẤP) --------
st.markdown(
    """
    <div class="info-box" style="border-left: 5px solid #1976d2; display: flex; align-items: center; gap: 15px;">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" width="35">
        <div>
            <h5 style="margin: 0; color: #1565c0;">Instructor: Bùi Tiến Đức</h5>
            <a href="https://orcid.org/" target="_blank" style="text-decoration:none; color:#555; font-size:14px;">
                Researcher & Lecturer at UEF
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------- COPYRIGHT --------
st.markdown(
    """
    <div style="text-align:center; margin-top:30px; font-size:13px; color:#888; font-family: monospace;">
        © 2025 – Topic 5: Sentiment Analysis Project | Built with Streamlit & Python 🐍
    </div>
    """,
    unsafe_allow_html=True
)
