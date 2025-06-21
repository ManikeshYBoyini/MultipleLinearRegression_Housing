Launch jupyter from anaconda navigator

1. Go to the location where api_code and visualization_dashboard.py files are located. 
2. Launch a terminal from juypter notebook 
3. CD to the file location of api_code
4. Run this code 'uvicorn api_code:api --reload'
5. Launch an other terminal from jupyter notebook
6. CD to the file location of visualization_dashboard.py 
7. Run this code 'streamlit run Visualization_Dashboard.py'

this will open a 'Localhost' where you can get the predictions by giving in the feature inputs. 

