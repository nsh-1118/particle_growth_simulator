
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Precursor Particle Growth Simulator", layout="centered")

st.title("🔬 Precursor Particle Growth Simulator")
st.markdown("시뮬레이션 조건을 설정하고 입자 성장 트렌드를 확인해보세요.")

# Sidebar - input parameters
with st.sidebar:
    st.header("⚙️ 실험 조건")
    pH = st.slider("pH 값", 8.0, 12.0, 10.5, 0.1)
    ammonia_ratio = st.slider("암모니아/금속 몰비", 0.5, 3.0, 1.5, 0.1)
    reaction_time = st.slider("반응 시간 (h)", 0.5, 10.0, 2.0, 0.5)

# Simulate particle size (mock function)
def simulate_growth(pH, ammonia_ratio, time):
    k = 0.3 + (ammonia_ratio - 1.5) * 0.05 - (pH - 10.5) * 0.03
    time_array = np.linspace(0, time, 100)
    size_array = 300 * (1 - np.exp(-k * time_array))
    return time_array, size_array

t, size = simulate_growth(pH, ammonia_ratio, reaction_time)

# Plotting
fig, ax = plt.subplots()
ax.plot(t, size, color='green')
ax.set_title("입자 크기 성장 곡선")
ax.set_xlabel("시간 (h)")
ax.set_ylabel("입자 크기 (nm)")
st.pyplot(fig)
