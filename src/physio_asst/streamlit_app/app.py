import streamlit as st


st.set_page_config(page_title="Physiotherapy Diagnosis Assistant", page_icon="🩺", layout="wide")
st.title("🩺 PhysioAsst: Radiology-based Assistant")
st.markdown(
    "<h5 style='color:gray; font-weight:400; margin-top:-10px;'>"
    "Analyze imaging, customize rehab plans, support decision-making."
    "</h5>",
    unsafe_allow_html=True,
)

choice = st.selectbox(
    "Understand about the body region that you're going to analyze:",
    ["Shoulder", "Knee", "Lumbar / lower back", "Placeholder"]
)

if choice == "Shoulder":
    st.markdown(
        '[💪 Understanding shoulder pain →](https://purephysiotherapy.co.uk/understanding-shoulder-pain-causes-risks-and-physiotherapy-treatments/)',
        unsafe_allow_html=True
    )
    st.text("List of possible shoulder conditions:")

    st.markdown("""
        - Shoulder Impingement – 肩部撞击综合征  
        - Degenerative Rotator Cuff Tear – 退行性肩袖撕裂  
        - Calcific Tendinopathy – 钙化性肌腱病  
        - Thoracic Outlet Syndrome – 胸廓出口综合征  
        - Acute Torticollis – 急性斜颈  
        - Benign Joint Hypermobility Syndrome – 良性关节过度活动综合征  
        - Clavicle Fracture – 锁骨骨折  
        - Acromioclavicular Joint Injury – 肩锁关节损伤  
        - Shoulder Osteoarthritis (OA) – 肩关节骨关节炎  
        - Shoulder Dislocation – 肩关节脱位  
        - Whiplash Disorders – 甩鞭伤综合征  
        - Frozen Shoulder – 冻结肩 / 肩周炎  
        - Rotator Cuff Tendinopathy – 肩袖肌腱病变  
        - Biceps Tendinopathy – 肱二头肌肌腱病变  
    """)

elif choice == "Lumbar / lower back": 
    st.markdown(
        '[🏋️‍♂️ Understanding lumbar pain →](https://purephysiotherapy.co.uk/understanding-lower-back-pain-and-sciatica-causes-risks-and-physiotherapy-treatments/)',
        unsafe_allow_html=True
    )
    st.text("List of possible lumbar (lower back) conditions:")
    st.markdown("""
        - Coccydynia — 尾骨痛  
        - Lumbar Spine Osteoarthritis (OA) — 腰椎骨关节炎  
        - Mechanical Back Pain — 机械性背痛  
        - Lumbar Disc Injury — 腰椎间盘损伤  
        - Spondylolysis — 椎弓峡部裂  
        - Sacroiliac Joint Dysfunction — 骶髂关节功能障碍  
        - Femoral Nerve Radiculopathy — 股神经根病变  
        - Ankylosing Spondylitis — 强直性脊柱炎  
        - Spondylolisthesis — 椎体滑脱  
        - Benign Joint Hypermobility Syndrome — 良性关节过度活动综合征  
        - Cauda Equina Syndrome — 马尾综合征  
        - Lumbar Spinal Stenosis — 腰椎管狭窄症  
        - Deep Gluteal/Piriformis Syndrome — 深臀肌/梨状肌综合征  
        - Low Back Pain and Sciatica — 腰痛及坐骨神经痛  
        - Greater Trochanteric Pain Syndrome — 股骨大转子疼痛综合征  
        - Femoroacetabular Impingement — 髋臼撞击综合征  
        """)
    
elif choice == "Knee":
    st.markdown(
        '[🦵 Understanding knee pain →](https://purephysiotherapy.co.uk/understanding-knee-pain-causes-risks-and-physiotherapy-treatments/)',
        unsafe_allow_html=True
    )
    st.text("List of possible knee conditions:")
    st.markdown("""
        - Medial Collateral Ligament Sprain — 内侧副韧带扭伤  
        - Quadricep Strain — 股四头肌拉伤  
        - Degenerative Meniscus — 退行性半月板病变  
        - Femoral Nerve Radiculopathy — 股神经根病变  
        - Bowed Knees — 膝内翻 / 膝外翻  
        - Benign Joint Hypermobility Syndrome — 良性关节过度活动综合征  
        - Patellofemoral Pain Syndrome (PFPS) — 髌股疼痛综合征  
        - Iliotibial Band Syndrome — 髂胫束综合征  
        - Knee Osteoarthritis — 膝关节骨关节炎  
        - Patellar Tendinopathy — 髌腱病 / 髌腱炎  
        - Osgood-Schlatter Disease — 奥斯古德-施拉特病  
        - Meniscus Injury — 半月板损伤  
        - Knee Replacement Surgery — 膝关节置换术  
        - Lateral Collateral Ligament (LCL) Injury — 外侧副韧带损伤  
        - Fat Pad Impingement — 脂肪垫撞击综合征  
        - Quadriceps Tendinopathy — 股四头肌腱病变  
        - Anterior Cruciate Ligament (ACL) Injury — 前交叉韧带损伤  
        - Pes Anserine Bursitis — 鹅足滑囊炎  
        - Baker’s Cyst — 贝克囊肿  
        - Hamstring Strain/Tear — 腘绳肌拉伤/撕裂  
        - Patella Dislocation — 髌骨脱位  
        """)

else: 
    st.text("all other conditions coming soon...")



# -------------------------------------
# Footer
# -------------------------------------
st.markdown("---")
st.warning(
    "⚠️ Use of this app is at your own discretion and responsibility. "
    "AI, like human doctors, can make mistakes."
)
