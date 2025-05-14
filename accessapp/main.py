# import streamlit as st
# import subprocess
# import platform
# import os
# import sys
# import openai
# import docx
# def run_application(path):
#     try:
#         if not os.path.isfile(path):
#             st.error("❌ The file does not exist.")
#             return
#
#         # If it's a Python file, run it as a Streamlit app
#         if path.endswith(".py"):
#             subprocess.Popen([sys.executable, "-m", "streamlit", "run", path], shell=True)
#             st.success(f"✅ Launched Streamlit app: {path}")
#         else:
#             # Handle general file execution based on OS
#             if platform.system() == "Windows":
#                 os.startfile(path)
#             elif platform.system() == "Darwin":  # macOS
#                 subprocess.Popen(["open", path])
#             else:  # Linux
#                 subprocess.Popen(["xdg-open", path])
#             st.success(f"✅ Launched file: {path}")
#
#     except Exception as e:
#         st.error(f"⚠️ Failed to launch the application: {e}")
#
# def main():
#     st.title("🚀 Local App Launcher")
#
#     st.markdown("Enter the **full path** to a Streamlit `.py` file or any executable/script to launch it.")
#
#     path = st.text_input("🔗 File Path", placeholder="e.g. C:\\Users\\YourName\\Desktop\\project\\app.py")
#
#     if st.button("Run"):
#         if path:
#             run_application(path)
#         else:
#             st.warning("Please enter a valid path.")
#
#     st.divider()
#     st.caption(f"Current Python: `{sys.executable}`")
#
# if __name__ == "__main__":
#     main()

# streamlit_app_launcher.py

import streamlit as st
import subprocess
import platform
import os
import sys

def install_requirements(path):
    """Install dependencies from requirements.txt if available."""
    base_dir = os.path.dirname(path)
    requirements_path = os.path.join(base_dir, "requirements.txt")

    if os.path.isfile(requirements_path):
        try:
            st.info("📦 Installing dependencies from requirements.txt...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_path])
            st.success("✅ Dependencies installed.")
        except subprocess.CalledProcessError as e:
            st.error(f"❌ Failed to install requirements:\n{e}")
    else:
        st.info("ℹ️ No requirements.txt found in app directory.")

def run_application(path):
    try:
        if not os.path.isfile(path):
            st.error("❌ The file does not exist.")
            return

        # Install dependencies if requirements.txt exists
        if path.endswith(".py"):
            install_requirements(path)

            subprocess.Popen([sys.executable, "-m", "streamlit", "run", path], shell=True)
            st.success(f"✅ Launched Streamlit app: {path}")
        else:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":
                subprocess.Popen(["open", path])
            else:
                subprocess.Popen(["xdg-open", path])
            st.success(f"✅ Launched file: {path}")

    except Exception as e:
        st.error(f"⚠️ Failed to launch the application: {e}")

def main():
    st.title("🚀 Local App Launcher with Dependency Management")

    st.markdown("Enter the **full path** to a Streamlit `.py` file or any executable/script to launch it. "
                "If a `requirements.txt` exists in the same folder, it will be auto-installed before launching.")

    path = st.text_input("🔗 File Path", placeholder="e.g. C:\\Users\\You\\Desktop\\project\\app.py")

    if st.button("Run"):
        if path:
            run_application(path)
        else:
            st.warning("Please enter a valid path.")

    st.divider()
    st.caption(f"Current Python: `{sys.executable}`")

if __name__ == "__main__":
    main()

