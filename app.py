import streamlit as st
from student import Student, StudentManager

manager = StudentManager()

st.title("🎓 Student Management System")

menu = ["Add Student", "View Students", "Search Student", "Delete Student"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Student":
    st.subheader("Add New Student")
    id = st.text_input("Student ID")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=5, max_value=30)
    student_class = st.text_input("Class")
    email = st.text_input("Email")
    
    if st.button("Add"):
        new_student = Student(id, name, age, student_class, email)
        manager.add_student(new_student)
        st.success("Student Added Successfully!")

elif choice == "View Students":
    st.subheader("All Students")
    students = manager.view_students()
    for s in students:
        st.write(vars(s))

elif choice == "Search Student":
    st.subheader("Search Student by ID")
    search_id = st.text_input("Enter Student ID to Search")
    if st.button("Search"):
        student = manager.find_student(search_id)
        if student:
            st.write(vars(student))
        else:
            st.warning("Student Not Found!")

elif choice == "Delete Student":
    st.subheader("Delete Student by ID")
    del_id = st.text_input("Enter ID to Delete")
    if st.button("Delete"):
        manager.delete_student(del_id)
        st.success("Student Deleted Successfully!")

#### Login code
st.sidebar.title("Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if username == "abd" and password == "123":
    # Show full app
    st.success("Logged in successfully!")
    # Rest of your app code here...
else:
    st.warning("Please login with correct credentials to access the system.")


del_id = st.text_input("Enter ID to Delete")
if st.button("Delete"):
    confirm = st.checkbox("Confirm Delete")
    if confirm:
        manager.delete_student(del_id)
        st.success("Student Deleted!")
    else:
        st.info("Please confirm to delete student.")


### Studdent pics add 


# uploaded_file = st.file_uploader("Upload Student Photo", type=["jpg", "png"])
# image_path = None

# if uploaded_file:
#     image_path = f"images/{id}.jpg"
#     with open(image_path, "wb") as f:
#         f.write(uploaded_file.getbuffer())

# if student:
#     col1, col2 = st.columns([1, 2])
#     with col1:
#         if student.image_path:
#             st.image(student.image_path, width=150)
#         else:
#             st.image("default.png", width=150)
#     with col2:
#         st.markdown(f"**Name:** {student.name}")
#         st.markdown(f"**Age:** {student.age}")
#         st.markdown(f"**Class:** {student.student_class}")
#         st.markdown(f"**Email:** {student.email}")

import os

student_id = st.text_input("Enter Student ID")
uploaded_file = st.file_uploader("Upload Photo", type=["jpg", "png"])
image_path = None

# Check or create images folder
if not os.path.exists("images"):
    os.makedirs("images")

if uploaded_file and student_id:
    image_path = f"images/{student_id}.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Image uploaded successfully!")



