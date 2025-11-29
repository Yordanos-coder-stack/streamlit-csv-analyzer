import sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    # Launch Streamlit programmatically so you can run `python launch_streamlit.py`
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(stcli.main())
    
