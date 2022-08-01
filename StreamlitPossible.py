import streamlit as st
import pickle
import pandas as pd


rf_model = pickle.load(open('app/rf_pipe.sav', 'rb'))
svm_model = pickle.load(open('app/svm_pipe.sav', 'rb'))
nn_model = pickle.load(open('app/nn_pipe.sav', 'rb'))

# all models to select from
all_models = {
    "Random forest": rf_model,
    "Support vector machine": svm_model,
    "Neural network": nn_model,
}

# all countries to select from
countries = [
    "US",
    "HK",
    "ES",
    "GB",
    "CA",
    "AU",
    "IT",
    "CH",
    "DE",
    "MX",
    "NZ",
    "DK",
    "JP",
    "PL",
    "SE",
    "FR",
    "NL",
    "IE",
    "SI",
    "SG",
    "BE",
    "NO",
    "GR",
    "LU",
    "AT",
]

# all categroeis/sub-categories to select from
categories = {
    "Food": [
        "Restaurants",
        "Vegan",
        "Spaces",
        "Drinks",
        "Food Trucks",
        "Farms",
        "Events",
        "Bacon",
        "Community Gardens",
        "Cookbooks",
        "Small Batch",
    ],
    "Film & Video": ["Comedy", "Documentary"],
    "Theater": ["Spaces", "Plays"],
    "Journalism": ["Print", "Video", "Photo", "Audio", "Web"],
    "Design": [
        "Interactive Design",
        "Toys",
        "Product Design",
        "Graphic Design",
        "Typography",
        "Civic Design",
        "Architecture",
    ],
    "Comics": ["Graphic Novels", "Webcomics"],
    "Music": ["Rock", "Punk", "Pop", "R&B"],
    "Technology": ["Software", "Sound"],
    "Publishing": [
        "Fiction",
        "Letterpress",
        "Literary Spaces",
        "Literary Journals",
        "Poetry",
    ],
    "Art": ["Conceptual Art"],
}


def predict_outcome(model, data):
    # build dict of data to predict from
    dict_data = {
        "country": data[0],
        "parent_name": data[1],
        "name": data[2],
        "goal_usd": data[3],
        "total_days_active": data[4],
        "launch_time": data[5],
    }

    # build dataframe and transpose to ensure data is in the right structure
    data = pd.DataFrame.from_dict(dict_data, orient="index").T

    # return prediction
    return model.predict(data)


def main():
    st.title("Predict your Kickstarter's Success!")

    st.write('Play around with the parameters on the left and hit the button to predict the outcome.')

    current_model = st.sidebar.selectbox("Select the model you want to use", all_models)

    # get user input for inputs to the model prediction
    country = st.sidebar.selectbox("The country the Project is based in", countries)
    parent_name = st.sidebar.selectbox("Category", categories)
    name = st.sidebar.selectbox("Sub-Category", categories[parent_name])
    goal_usd = st.sidebar.text_input("target funding goal ($USD)", value=0)
    total_days_active = st.sidebar.text_input(
        "How long will the project be live? (days)", value=0
    )
    launch_time = st.sidebar.text_input(
        "How long will the project be visible before going live? (days)", value=0
    )

    # create button to generate prediction
    if st.button("Predict the outcome!"):
        prediction = predict_outcome(
            all_models[current_model],
            [country, parent_name, name, goal_usd, total_days_active, launch_time,],
        )
        if prediction[0] == "successful":
            st.write("The project is predicted to be succesfull!")
        else:
            st.write("The project is predicted to fail.")

    # short section describing each model
    st.markdown("## More about the model")

    if current_model == "Support vector machine":
        st.markdown(
            "### Support Vector Machine (SVM)\nThe Support vector machine was run using a linear kernel, and the gradient was iterated 500 times. This model yeilded a testing accuracy of 67%, with results heavily skewed toward the 'successful' project state, likely because of the imbalanced nature of the dataset. This result falls short of the Stanford paper of 79% accuracy, and is probably attirbuted to the lack of under/over sampling of the data."
        )
        st.image('images/SVM_report.png')
    elif current_model == "Neural network":
        st.markdown(
            "### SKlearn's Neural Network\nSKlearn's implementation of a multi-layer perceptron classifier was used with the lbfgs solver and an architecture of (input,4,2,1). The model achieved an accuracy of 80%, equivalent to the 80% achieved in the Stanford paper. Given more data processing and feature engineering, this model could see significant improvements in performance as it faces similar problems to the SVM with the imbalanced dataset."
        )
        st.image('images/nn_report.png')
    else:
        st.markdown(
            "### Random Forest\nSKlearn's RandomForest was used with no changes to the hyperparameters and returns an accuracy of 80% for the testing data, this aligns very closely to the results obained in the Stanford paper."
        )
        st.image('images/Random_forest_report.png')

    st.markdown(
        "If you want to know more about this project, the github repo can be seen [here](https://github.com/Epicosp/Predicting-Crowdfunding-Outcomes)"
    )


if __name__ == "__main__":
    main()