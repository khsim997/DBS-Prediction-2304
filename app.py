#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)


# In[ ]:


import joblib
@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        rate = float(request.form.get("rate"))
        print(rate)
        model=joblib.load("DBS_prediction")
        pred=model.predict([[rate]])
        return(render_template("index.html", result=pred))
    else:
        return(render_template("index.html", result="waiting"))
if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:




