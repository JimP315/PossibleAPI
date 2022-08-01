import streamlit as st
#import pickle
import pandas as pd



# all advisers to select from
all_advisers = [
    "Jim Pxxxxxr - Adviser Ratings 4.95", 
    "Jon Mxxxxw - Adviser Ratings 4.8",
    "Blaine Mxxxr - Adviser Ratings 4.75",
    "Maria Axxxn - Adviser Ratings 4.7",  
]

# all services to choose from 
services = [
    "Investment only",
    "Life Insurance Review/Advice",
    "Super Investment / Rollover Advice",
    "Super contribution Advice",
    "Lending/Mortgage/Margin Lending Advice",
    "Estate Planning Advice",
    "Retirement Planning Advice",
    "Centrelink and/or Aged Care Advice",
    "3 - 4 of the Above services",
    "Comprehensive Advice, ie all of the above",
  
]

# risk profile that suits the potential client 
risk_profile = [
    "Balanced", 
    "Balanced Growth", 
    "Growth",
 
]


# investment range you are looking to invest 

investment_amount = [ 
    ">= $10,000", 
    ">= $75,000", 
    ">= $300,000",
    ">= $750,000",

]
# what will we try to predict here....maybe end value based on risk profile 
def predict_outcome(model, data):
    # build dict of data to predict from
    dict_data = {
        "services": data[0],
        "risk profile": data[1],
        "investment_aud": data[2],
        "investment_regular": data[3],
        "investment_timeframe": data[4],
        "investment_goal": data[5],
    }

    # build dataframe and transpose to ensure data is in the right structure
    data = pd.DataFrame.from_dict(dict_data, orient="index").T

    # return prediction
    return model.predict(data)


def main():
    st.title("Get started on your journey to Financial Success!")

    st.write('Let us know a bit of how we can help you as well as your appetite for risk.')

    current_adviser = st.sidebar.selectbox("Which adviser would you like to work with to achieve financial success?", all_advisers)

    # get user input for inputs to the model prediction
    services = st.sidebar.selectbox("How are we able to assist you", services)
    risk_appetite = st.sidebar.selectbox("Risk Profile", risk_profile)
    investment_aud = st.sidebar.text_input("Initial Investment Amount ($AUD)", investment_amount)
    investment_timeframe = st.sidebar.text_input(
        "How long will you likely invest for (years)", value=0
    )
    investment_regular = st.sidebar.text_input(
        "How much are you willing to invest on a monthly basis in order to achieve your goal? ($AUD)", value=0
    )
    investment_goal = st.sidebar.text_input(
        "What is your end goal in terms of expected capital value target? ($AUD)", value=0
    )

    # create button to generate prediction - this may be more along the lines of the expected rate of return needed to achieve goal or the likely value in the expected timeframe. 
    if st.button("Likely Investment outcomes!"):
        prediction = predict_outcome(
            all_models[current_adviser],
            [services, risk_appetite, investment_aud, investment_timeframe, investment_regular, investment_goal,],
        )
        if prediction[0] == "successful":
            st.write("You are likely to achieve your financial goal!")
        else:
            st.write("You may have a funding shortfall :( ")

    if risk_profile == "Balanced":
     { 
        if investment_amount > $750,000
            st.image("\MC_summitbal_sim_plot.png"
            )
        elif investment_amount > $300,000 
            st.image(#image for Ascent balanced
            ) 
        elif investment_amount > $75,000 
            st.image(#image for Expedition balanced
            ) 
        else: 
            st.image(#image for Foundation balanced
            )         
     }
    elif risk_profile == "Balanced Growth":
     {     
         if investment_amount > $750,000
            st.image("\MC_summitbg_sim_plot.png"
            )
        elif investment_amount > $300,000 
            st.image(#image for Ascent balanced growth
            ) 
        elif investment_amount > $75,000 
            st.image(#image for Expedition balanced growth
            ) 
        else: 
            st.image(#image for Foundation balanced growth
            )
     }
    elif risk_profile == "Growth":
     {     
         if investment_amount > $750,000
            st.image("\MC_summitgrow_sim_plot.png"
            )
            st.markdown("### ")
        elif investment_amount > $300,000 
            st.image(#image for Ascent growth
            ) 
        elif investment_amount > $75,000 
            st.image(#image for Expedition growth
            ) 
        else: 
            st.image(#image for Foundation growth
            )
     }
    st.markdown("## More about our University qualified Advisers")

    if current_adviser == "Jim Pxxxxr - Adviser Ratings 4.95":
        st.markdown(
            "### Jim's background:  Bachelor of Commerce (Hon), University of Manitoba, 1992; Diploma of Financial Planning; Accredited Aged Care Specialist, 2016; Stanford Executive Program; Self Managed Superannuation Accreditation; ASX Listed Products Accreditation, Monash FinTech Bootcamp", 
        )
        st.image('images\Jim.jpg')
    elif current_adviser == "Jon Mxxxxw - Adviser Ratings 4.8":
        st.markdown(
            "### Jon's background: Bachelor of Business, Queensland University of Technology, Australia, 2000; Advanced Diploma of Financial Planning ; Diploma of Financial Services (Financial Planning); Self Managed Superannuation Accreditation; ASX Listed Products Accreditation; Diploma of Financial Services (Finance/Mortgage Broking)"
        )
        st.image('images\p3fplogo.jpg"')
    elif current_adviser == "Blaine Mxxxr - Adviser Ratings 4.75":
        st.markdown(
            "### Blaine's background: Bachelor of Business; Advanced Diploma of Financial Planning, 2020; Accredited Aged Care Specialist, 2019; Diploma of Financial Planning; ETF Certification."
        )
        st.image('images/Blaine.jpg')
    else: 
        st.markdown(
            "### Maria's background:  Accredited Aged Care Specialist, 2020; Advanced Diploma of Financial Planning; Diploma of Financial Planning; Master of Science Business Analysis & Finance; Bachelor of Arts Business Economics"
        )
        st.image('images/Maria.jpg')


if __name__ == "__main__":
    main()