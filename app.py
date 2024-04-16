import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

st.title('Rocket Simulator')

m=50      #weight of the rocket in kg
g=9.81         #The gravity
p=1.091        #The air density
r=0.5          #The radio of the cross sectional area
ve=325         #The exhaust speed
Cd=0.15        #The drag coefficient
dt=1        #The time-step
mp0=100        #The initial weight of the rocket at time t=0
tf=40          #The total time of simulation


st.number_input('Enter the weight of the rocket in kg', value=50)
st.number_input('Enter the gravity', value=9.81)
st.number_input('Enter the air density', value=1.091)
st.number_input('Enter the radio of the cross sectional area', value=0.5)
st.number_input('Enter the exhaust speed', value=325)
st.number_input('Enter the drag coefficient', value=0.15)
st.number_input('Enter the time-step', value=1)
st.number_input('Enter the initial weight of the rocket at time t=0', value=100)
st.number_input('Enter the total time of simulation', value=40)

A=np.pi*(r**2) #The cross sectional area
N=int((tf-0)/dt)+1    #The number of steps
t=np.linspace(0,tf,N) #The array for the time


mr=[]
for i in range(0,N):
    if (t[i]<5):
        mr.append(20)
    else:
        mr.append(0)

#This function is mr.
def f(x):
    if (x<=5):
        return 20
    else:
        return 0

def integral(tf,t0):
    N=int(1e6)             #The total number of intervals.
    h=abs((tf-t0)/N)       #The increment of values.
    P1=(h/3)*(f(t0)+f(tf)) #The Part 1 of the equation.
    OS=0; ES=0            #Initialize the sums of values.
    #It's time to initialize the for loop
    for i in range(1,N-1):
        dx=t0+(i*h) #Here we decide the value to use
        if (i%2==0): #If i is an even, then use the Even sum 
            ES+=2*f(dx)
        else:
            OS+=4*f(dx) #If i is an odd, then use the Odd sum
    return P1+(h/3)*(OS+ES) #Return the final value of the integral

def mp(t):
    return mp0-integral(tf=t,t0=0) #The values to use in our Simpson method

def euler(mr,ve,m,dt,g,p,A,Cd):
    v=np.zeros(N)
    h=np.zeros(N)
    for i in range(0,N-1):
        F1=(mr[i]*ve)/(m+round(mp(t[i]),2))
        F2=(p*v[i]*abs(v[i])*A*Cd)/(2*(m+round(mp(t[i]),2)))
        v[i+1]=v[i]+dt*(F1-F2-g)
        h[i+1]=h[i]+(dt*v[i])
    return v,h

if st.button('Simulate'):
    with st.spinner('Simulating...'):
        ## the velocity and height of the rocket
        v,h=euler(mr,ve,m,dt,g,p,A,Cd)
        fig = px.line(x=t, y=h, labels={'x':'Time', 'y':'Height'}, title='Rocket Simulator')
        fig2 = px.line(x=t, y=v, labels={'x':'Time', 'y':'Velocity'}, title='Rocket Simulator')
        st.plotly_chart(fig, usecontainer_width=True)
        st.plotly_chart(fig2, usecontainer_width=True)
