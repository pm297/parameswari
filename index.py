import streamlit as st
import sqlite3
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import base64
from PIL import Image
import cv2

# ================ Background image ===
# st.set_page_config(page_title="Data Explorer", layout="wide")

st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Apollo An Lightweight Multilingual Medical LLM"}</h1>', unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('7.jpg')

# ==============================================================

# Initialize the database and create the users table
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')
conn.commit()


conn_a = sqlite3.connect('admins.db')
ca = conn_a.cursor()
ca.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username_a TEXT PRIMARY KEY,
        password_b TEXT
    )
''')
conn_a.commit()

st.title('Login and Register System')

menu = st.sidebar.selectbox("Select Option", ["Login", "Register",'Login as Admin'])
import os 
if menu == "Register":
    st.subheader("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    os.makedirs('DB/'+username, exist_ok=True)

    col1,col2 = st.columns(2)
    
    
    
    with col2:
        
        import streamlit as st
        import cv2
        import numpy as np
        import os
        from PIL import Image
        
        def process_image(uploaded_file, username):
            # Read the image file with PIL
            pil_image = Image.open(uploaded_file)
            
            # Convert the PIL image to a NumPy array
            image = np.array(pil_image)
            
            # Check if the image is RGBA (i.e., it has an alpha channel)
            if image.shape[-1] == 4:  # RGBA
                # Convert RGBA to RGB
                image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
            else:
                # Convert RGB to BGR
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Define the directory path
            directory = f'DB/{username}/'
            
            # Create the directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            # Define the full path for saving the image
            file_path = os.path.join(directory, username+'.jpg')
            
            # Save the image
            cv2.imwrite(file_path, image)
            
            return file_path
        
        # Streamlit app
        def main():
            
            # File uploader widget
            uploaded_file = st.file_uploader("Upload Medical Image During Register...", type=["png", "jpg", "jpeg"])
            
            if uploaded_file is not None:
                # Display the uploaded image
                st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
                
                # Input field for username
                username = st.text_input("Enter your username:")
                
                if st.button('Save Image'):
                    if username:
                        file_path = process_image(uploaded_file, username)
                        st.success(f'Image saved successfully at {file_path}')
                    else:
                        st.error('Please enter a username.')
        
        if __name__ == "__main__":
            main()
        
                
    with col1:
        st.title('Upload Medical Report To Register')


    # os.makedirs('Cloud/'+username, exist_ok=True)
     
    # with st.sidebar:
         
 
    #      # Create a file uploader widget
    #      uploaded_file = st.file_uploader("Choose a file...", type=["txt"])
         
    #      if uploaded_file is not None:
    #          # Read the file content
    #          file_content = uploaded_file.read().decode("utf-8")    
             
    #          st.write(file_content)

 
    #      # Define the path to the source file and the target directory
    #      source_file_path = uploaded_file
    #      target_directory = 'Cloud/'+username+'/'+uploaded_file.name
    #      st.write(source_file_path)
    #      st.write(target_directory)
         

    #      try:

    #          # Write the contents to the destination file
    #          with open(target_directory, 'w+') as destination_file:
    #              destination_file.write(file_content)
             
    #          st.write(f"File successfully copied to '{target_directory}'.")
         

    #      except Exception as e:
    #          st.write(f"An error occurred: {e}")
         
    #      entries = os.listdir('Cloud/'+username)
    #      st.write(entries)           
        

        
    if st.checkbox("Register"):
        if username and password:
            try:
                c.execute('''
                    INSERT INTO users (username, password) VALUES (?, ?)
                ''', (username, password))
                conn.commit()

                
                st.success('Hi !!!'+username+"Your Credentials and Medical Image Registered successfully!")
    

            except sqlite3.IntegrityError:
                st.error("Dear "+username+" !!! Username already exists.")
        else:
            st.error("Please fill in both fields.")
            
# =====================================================================

# =====================================================================

# ---------------------------------------------------------------------

# =====================================================================

# =====================================================================

elif menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    
    if st.checkbox("Login"):
        if username and password:
            c.execute('''
                SELECT * FROM users WHERE username = ? AND password = ?
            ''', (username, password))
            user = c.fetchone()
            if user:
                st.success("Logged in successfully!")
                # import subprocess
                # subprocess.run(['streamlit','run','Main.py'])
                
     
            else:
                st.error("Invalid username or password.")
        else:
            st.error("Please fill in both fields.")            
        
        CB2 = st.checkbox('Click To Upload Medical Image')
        if CB2:
            
            import os
            import numpy as np
            import cv2
            import matplotlib.pyplot as plt
            
            # Define the directories and their corresponding labels
            # directories = {
            #     'benign': 0,
            #     'malignant': 1,
            #     'normal': 2
            # }

            # Path to the main dataset directory
            dataset_dir = 'DB/'
            
            # Discover all subdirectories in the dataset directory
            subdirectories = [d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))]
            
            # Create a mapping of directory names to labels
            directories = {subdir: idx for idx, subdir in enumerate(subdirectories)}


            
            dot = []
            labels_target = []
            
            for directory, labels in directories.items():
                dir_path = 'DB/'+directory+'/'
                label = labels
                images = os.listdir(dir_path)
                
                for img in images:
                    try:
                        img_path = os.path.join(dir_path, img)
                        img_ = plt.imread(img_path)
                        img_resize = cv2.resize(img_, (224, 224))
                        dot.append(np.array(img_resize))
                        labels_target.append(label)
                    except Exception as e:
                        print(f"Error processing image {img_path}: {e}")

            

            import streamlit as st
            import cv2
            import numpy as np
            import os
            from PIL import Image
            


            # File uploader widget
            uploaded_filenew = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
            
            if uploaded_filenew is not None:
                # Display the uploaded image
                    img_1 = plt.imread(uploaded_filenew)
                    img_resize1 = cv2.resize(img_1, (224, 224))       
                    
            for ii in range(len(dot)):
                if np.mean(dot[ii][:,:,0] - img_resize1[:,:,0]) == 0:
                    IDX = ii
                else:
                    IDX = 0
            st.write('Index',IDX)        
            OSS = os.listdir('DB/')[IDX]
            st.write(OSS)
            st.write(username)
            st.success('Uploaded Done !!! ✅')



                
                
                
            # if OSS == username:
                # CB3 = st.checkbox('Click To Chat !!!')
                # if CB3:
                #     import subprocess
                #     subprocess.run(['streamlit','run','mss.py'])

                
                
                
            
            
    
                
            # else:
                # st.error('Upload Failed  ⛔')
        CB4 = st.checkbox('Click To Chat Window')
        if CB4:
                    import subprocess
                    subprocess.run(['streamlit','run','mss.py'])
                        

elif menu == 'Login as Admin':
    st.subheader("Admin Login")
    username_a = st.text_input("Admin ID")
    password_a = st.text_input("Admin Password", type='password')
    
    if st.button("Login Admin"):
        if username_a and password_a:
            ca.execute('''
                SELECT * FROM users WHERE username_a = ? AND password_a = ?
            ''', (username_a, password_a))
            admin = ca.fetchone()
            if admin:
                st.success("Admin Logged in successfully!")
                
                
                
                # Connect to the SQLite database
                conn_j = sqlite3.connect('users.db')
                cj = conn_j.cursor()
                
                # Query to select all records from the 'users' table
                cj.execute('SELECT * FROM users')
                
                # Fetch all results from the executed query
                rows = cj.fetchall()
                
                # Print the contents of the 'users' table
                st.write("User Details")
                for row in rows:
                    st.write(row)
                
                # Close the database connection
                conn_j.close()
                
                import pandas as pd

                # Read the CSV file
                df = pd.read_csv('Dataset.csv')  # Adjust the filename as needed
                st.write('Train Data')
                st.write(df)
                # # Extract the column containing product names
                # product_column = df['Name']  # Adjust the column name as needed
                # sty = df['Status']  # Adjust the column name as needed
                
                # # Remove duplicate product names
                # unique_products = product_column.drop_duplicates().sort_values()
                
                # # Display the unique product names
                # st.write('----')

                # st.write("User Names / Status")
                # for product in unique_products:
                #     for stt in sty:
                        
                #         st.write('----')
                #         st.write(product,'-',stt)

                
            else:
                st.error("Invalid ID or password.")
        else:
            st.error("Please fill in both fields.")
# Close the database connection
conn_a.close()

conn.close()
