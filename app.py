import streamlit as st
from factorial import factorial

def main():
    # Tựa đề ứng dụng
    st.title("Ứng dụng Tính Toán Cơ Bản")
    st.header("Tính Giai Thừa của Một Số Tự Nhiên")
    st.write("Ứng dụng này cho phép bạn tính giai thừa của một số tự nhiên. Vui lòng nhập số cần tính giai thừa vào ô dưới đây và nhấn nút 'Calculate'.")
    
    # Nhập số tự nhiên từ người dùng
    number = st.number_input("Nhập một số tự nhiên:", min_value = 0, max_value = 900, value = 0, step = 1)

    # Tạo nút tính toán
    if st.button("Calculate"):
        result = factorial(number)
        st.write(f"Giai thừa của {number} là: {result}")

if __name__ == "__main__":
    main()