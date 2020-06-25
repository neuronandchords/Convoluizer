import streamlit as st
import math

def predict_pad():
    st.write("Enter Input size as N*N")
    n= st.slider('N',min_value=0,max_value=1080)

    st.write("Enter the filter size as F*F")
    f= st.slider('F',min_value=0,max_value=1080)

    st.write("No. of Filters to be applied ")
    nf=st.slider('Nf',min_value=0,max_value=1080)

    st.write("Enter stride as S units")
    s=st.slider('S',min_value=0,max_value=1080)

    st.write("Enter the output size as O*O")
    o=st.slider('O',min_value=0,max_value=1080)

    
    if(s==0):
        st.write("You cannot perform convolution with stride=0")
    else:
        st.write("You need to pad with P as ")
        st.write(math.floor((((o-1)*s)+f-n)/2))

def predict_output():
    st.write("Enter Input size as N*N")
    n= st.slider('N',min_value=0,max_value=1080)

    st.write("Enter the filter size as F*F")
    f=st.slider('F',min_value=0,max_value=1080)

    st.write("Enter stride as S units")
    s=st.slider('S',min_value=0,max_value=1080)

    st.write("Enter the padding as P units")
    p = st.slider('P',min_value=0,max_value=1080)

    if(s!=0):
        st.write("The output size in O*O would be")
        st.write(math.floor((n+2*p-f+1)/s))
    else:
        st.write("You cannot apply convolution with stride=0")

def predict_filter():
    st.write("Enter Input size as N*N")
    n= st.slider('N',min_value=0,max_value=1080)

    st.write("Enter stride as S units")
    s=st.slider('S',min_value=0,max_value=1080)

    st.write("Enter the padding as P units")
    p = st.slider('P',min_value=0,max_value=1080)

    st.write("Enter the output size as O*O")
    o=st.slider('O',min_value=0,max_value=1080)

    if(s==0):
        st.write("You cannot perform convolution with stride=0")
    else:
        st.write("You need to apply a filter of ")
        st.write(-1*math.floor((o-1)*s-n-2*p))

def predict_input():
    st.write("Enter Output size as O*O")
    o= st.slider('O',min_value=0,max_value=1080)

    st.write("Enter the filter size as F*F")
    f=st.slider('F',min_value=0,max_value=1080)

    st.write("Enter stride as S units")
    s=st.slider('S',min_value=0,max_value=1080)

    st.write("Enter the padding as P units")
    p = st.slider('P',min_value=0,max_value=1080)

    if(s==0):
        st.write("You could not have performed convolution with stride=0")
    else:
        st.write("The Input Size before convolutions in N*N was")
        st.write(math.floor((o-1)*s+f-(2*p)))

def predict_maxpool2d():
    st.write("Enter Input size as N*N")
    n= st.slider('N',min_value=0,max_value=1080)

    st.write("Enter the filter size as F*F")
    f=st.slider('F',min_value=0,max_value=1080)

    st.write("Enter stride as S units")
    s=st.slider('S',min_value=0,max_value=1080)

    st.write("Enter the padding as P units")
    p = st.slider('P',min_value=0,max_value=1080)

    st.write("The Output Size after Max_pool2d in O*O would be")
    if(s==0):
        st.write("You cannot perform convolution with stride=0")
    else:
        st.write("The Output Size after Max_pool2d in O*O would be")
        st.write(math.floor((n+(2*p)-f)/s)+1)

def predict_flatten():
    st.write("Enter Input size as N*N")
    n= st.slider('N',min_value=0,max_value=1080)

    st.write("Enter the no. of channels as C in N x N x C")
    c=st.slider('C',min_value=1,max_value=1080)

    st.write("The Output Size after Flatten in O*O would be")
    st.write(n*n*c)


st.title("CONVOLUIZER - Convolutions Made Easy")

st.write()
st.markdown("_Where does the difficulty lie? I am here to help you :)_")
option = st.selectbox("",("Knowing the output size","Knowing how much to pad for a certain output size","Knowing what filter to apply to get a certain output size","Knowing what was the initial input size before convolutions","Apply Max_Pool2d","Apply Flatten()"))

if(option=="Knowing the output size"):
    predict_output()
elif(option=="Knowing how much to pad for a certain output size"):
    predict_pad()
elif(option=="Knowing what filter to apply to get a certain output size"):
    predict_filter()
elif(option=="Apply Max_Pool2d"):
    predict_maxpool2d()
elif(option=="Apply Flatten()"):
    predict_flatten()
else:
    predict_input()

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")
st.markdown("**Developed by Amaya Srivastava**")
st.markdown("**_Github_**: _https://github.com/neuronandchords_ ",unsafe_allow_html=True)
st.markdown("**_Feedback/Fixes_:** Pull on Github")