import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Smart Broker: Insights", page_icon="📊", layout='wide', initial_sidebar_state="auto")

st.markdown("### Insights of available properties in Mumbai, India")
st.sidebar.header("Mumbai Properties Insights")

df = pd.read_csv('Datasets/property_list.csv')
df = df[df['Possession Status'].isin(['Ready to Move', 'Under Construction'])]
df.reset_index(drop=True, inplace=True)
df = df[df['Price'] <= 50000000]
df.reset_index(drop=True, inplace=True)

possession_status = st.multiselect(
        "Choose Property Possession Status", list(df['Possession Status'].unique()), []
    )
print(possession_status)
if possession_status:
    data = df[df['Possession Status'].isin(possession_status)]
    data.reset_index(drop=True, inplace=True)
else:
    data = df.copy()

price_range = st.slider("Select a price range", data['Price'].min(), data['Price'].max(), (data['Price'].min(), data['Price'].max()))

if price_range:
    data_p2 = data[data['Price'].between(price_range[0], price_range[1])]
    data_p2.reset_index(drop=True, inplace=True)
else:
    data_p2 = data.copy()

df_prop_type = data_p2['Possession Status'].value_counts().to_frame().reset_index()

fig1 = px.pie(df_prop_type, values='count', names='Possession Status', title="Property Possession Type")


df_location_property_count = data_p2.groupby(['Area Name'])['Units Available'].sum().to_frame().reset_index()
df_location_property_count = df_location_property_count.sort_values(by=['Units Available'], ascending=False)
df_location_property_count.reset_index(drop=True, inplace=True)
df_location_property_count = df_location_property_count[:10]


fig2 = px.bar(df_location_property_count, x='Area Name', y='Units Available', color='Area Name', title="Top 10 Areas with highest # of properties available")
fig2.update_xaxes(showticklabels=False)


cols = st.columns([1, 1])

cols[0].plotly_chart(fig1, theme=None, use_container_width = True)
cols[1].plotly_chart(fig2, theme=None)

data_p2 = data_p2[data_p2['Units Available'] >= 0]
data_p2.reset_index(drop=True, inplace=True)

col1, col2 = st.columns(2)

with col1:
    amenities_options = st.multiselect('Select Top Amenities Preferences:',('Swimming Pool', 'Lift', 'Club House', 'Gymnasium', 'Security', 'Parking', 'Prime location', 'Society','Sea facing', 'Skydeck','Kids Play Area','Vaastu Compliant'))

with col2:
    location_pref = st.multiselect(
        "Select Location Preferences:",
        ['Kalyan West', 'Bhoiwada', 'Rambaug Lane Number 4', 'Kalyan East', 'Chakki Naka', 'Nandivali Gaon', 'Tisgaon Naka', 'Oshiwara', 'Bandivali', 'Jogeshwari West', 'Malcom Baug', 'Amrut Nagar', 'Behram Baug', 'Indira Nagar', 'Jogeshwari Vikhroli Link Road', 'Jogeshwari East', 'Majas Wadi', 'Natwar Nagar', 'Hind Nagar', 'Sham Nagar', 'Dombivli East', 'Sonar Pada', 'Nandivli', 'Desai Village', 'Tilak Nagar', 'Gandhi Nagar Dombivli', 'Usarghar Gaon', 'Dahisar West', 'Kandarpada', 'Mhatre Wadi', 'Gomant Nagar', 'Leo Peter Wadi', 'Shanti Ashram', 'Navagaon', 'Ashok Van', 'Dahisar East', 'Anand Nagar', 'Vaishali Nagar Dahisar', 'Janta Nagar', 'Vaishali Nagar', 'Rawal Pada', 'Maratha Colony Dahisar', 'Shakti Nagar', 'Ketki Pada', 'NL Complex', 'Ghartan Pada', 'Balaji Nagar', 'Waghdevi Nagar', 'Virar West', 'Bolinj', 'Chikhal Dongari', 'Agashi', 'Tirupati Nagar', 'Y K Nagar', 'Gokul Township', 'Virat Nagar', 'Yashavant Nagar', 'Grant Road', 'Virar East', 'Bhalchandra Nagar', 'Dadar West', 'Shivaji Park', 'Kaka Sahab Dadarkar Chowk', 'Chandrakant Dhuru Wadi', 'Kabutarkhana Purandare Chowk', 'Prabodhankar Thakre Chowk', 'Bhawani Shankar', 'Jakhadevi Chowk', 'Suryavanshi Kshatriya Sabhagruha Chowk', 'Vile Parle West', 'Gulmohar Road', 'Suresh Colony', 'Irla', 'Sanyas Ashram Chowk', 'Kamla Nagar', 'Vile Parle East', 'Air India Colony', 'Shahaji Raje Marg', 'Parle Colony', 'Vasai West', 'Suyog Nagar', 'Chulne', 'Dindayal Nagar Vasai', 'Vasai East', 'Golani Naka', 'Dhumal Nagar', 'Kolshet Road', 'Pokharan Road Number 2', 'Balkum village', 'Majiwada', 'Kolshet', 'Manpada', 'Dhokali', 'Hiranandani Estate', 'Bhayandarpada', 'Vasant Vihar', 'Thane West', 'Panch Pakhdi', 'Teen Hath Naka', 'Patlipada', 'Naupada', 'Brahmand', 'Waghbil', 'Balkum Naka', 'Owale', 'Koliwada', 'Kolbad', 'Vartak Nagar', 'Savarkar Nagar', 'Vrindavan Society', 'Anand Nagar Thane West', 'Khopat', 'Pokharan Road Number 1', 'Kapurbawdi', 'Lok Puram', 'Shivai Nagar', 'Charai', 'Ram Maruti Road Naupada', 'Rabodi', 'Dhobi Ali', 'Wagle Industrial Estate', 'Mahagiri Koliwada', 'Lokmanya Nagar', 'Pawar Nagar', 'Uthalsar', 'Jambli Naka', 'Shivaji Nagar', 'Bhaskar Colony', 'Vishnu Nagar', 'Louis Wadi', 'Yashodhan Nagar', 'Gawand Baug', 'Meenatai Thakrey Chowk', 'Raunak Park', 'Runwal Nagar', 'Ghantali', 'Talav Pali', 'Vijay Nagar', 'Hariniwas Circle', 'Kopri', 'Thane East', 'Sion West', 'Chembur East', 'Sion East', 'Sion Koliwada', 'Santacruz West', 'Hasmukh Nagar', 'Willingdon Colony', 'North Ave', 'Saraswat Colony', 'MSES Colony', 'Potohar Nagar', 'Vithaldas Nagar', 'Dadar East', 'Hindu Colony', 'Dadar TT Circle', 'Mancharji Edhalji Joshi Chowk', 'AP Narayan Chowk', 'L Tilak Colony', 'Santacruz East', 'Kalina', 'Vidya Nagari', 'Sen Nagar', 'Kranti Nagar', 'Sundar Nagar, Kalina', 'Prabhat Colony', 'Kolivary', 'Anand Nagar Santacruz East', 'Prabhadevi', 'Adv RD Kowte Chowk', 'Century Bazaar', 'Shree Siddhivinayak Mandir Chowk', 'Babar Shaikh Chowk', 'Mira Road East', 'Mahajan Wadi', 'Geeta Nagar Mira Road', 'Penkarpada', 'Miragaon', 'Nalasopara West', 'Laxmiben Chheda Nagar', 'Samel Pada', 'Nalasopara East', 'Oswal Nagari', 'Naigaon West', 'Naigaon East', 'Goregaon East', 'Gokuldham', 'Film City Road', 'Jayprakash Nagar', 'Bimbisar Nagar', 'Ganesh Nagar', 'Kanya Pada', 'Laxmi Nagar', 'Nagari Nivara Parishad', 'Mali Nagar', 'Sai Baba Complex', 'Aarey Milk Colony', 'NNP Colony', 'Royal Palms Estate', 'Pandurang Wadi', 'Subhash Nagar', 'Churi Wadi', 'Azad Nagar', 'Shreyas Colony', 'Durgeshwari Welfare Society', 'Film City', 'Yeshodham', 'Indian Oil Nagar- Shivaji Nagar', 'Ram Nagar', 'CAMA Industrial Estate', 'Yashodham', 'ITT Bhatti', 'Vishveshwar Nagar', 'Agripada', 'Mumbai Central', 'RTO Colony', 'Churchgate', 'Matunga West', 'Joshi Wadi', 'Mahalaxmi Sindhi Colony', 'S Haralayya Chowk', 'Matunga East', 'Brhmanwada', 'Five Gardens', 'Kings Circle', 'Marine Lines East', 'Marine Lines', 'Churchgate station', 'Marine Drive', 'Malad East', 'Pathanwadi', 'Kurar Village', 'Triveni Nagar', 'Pushpa Park', 'Shivaji Nagar Malad East', 'Upper Govind Nagar', 'Primal Nagar', 'Dindoshi', 'Kokani Pada', 'Dhanji Wadi', 'Pathan Wadi Chowk', 'Dombivli West', 'Kopargaon', 'Mahim West', 'Asavari', 'Mahim East', 'Mahalaxmi Race Course', 'Lower Parel West', 'Chembur West', 'Rahul Nagar Chembur', 'Lower Parel East', 'Khar West', 'Juhu Koliwada', 'Old Khar', 'Khar Danda', 'Danda', 'Khar East', 'Golibar', 'RPF Colony', 'Kandivali West', 'Mahavir Nagar', 'Mahatama Gandhi Road Amrut Nagar', 'Dhanukar Wadi', 'Charkop Sector 2', 'Irani Wada', 'Charkop Sector 5', 'Charkop Industrial Estate', 'Charkop Sector 7', 'Charkop', 'Bander Pakhadi', 'Charkop Sector 4', 'Charkop Sector 9', 'Charkop Sector 3', 'Charkop Village', 'Charkop Sector 8', 'Charkop Sector 6', 'Charkop Sector 1', 'Jethava Nagar', 'Ekta Nagar Charkop', 'Shankar Pada', 'Goraswadi', 'Patel Nagar', 'Ganesh Nagar JJC Area', 'Fateh Baug', 'Kandivali East', 'Lokhandwala Twp', 'Alika Nagar', 'Thakur Village, Kandivali East', 'Akurli Nagar', 'Samata Nagar', 'Ashok Nagar Western Mumbai', 'Thakur Complex', 'Asha Nagar', 'Gautam Nagar', 'Appa Pada', 'Damodarwadi', 'Dattani Park', 'Singh Aghri Estate', 'Amboli', 'Laxmi Industrial Estate', 'Andheri West', 'Lokhandwala Complex', 'Four Bungalows', 'Seven Bungalows', 'Veera Desai Road', '4 Bunglows', 'Lallu Bhai Park', 'Azad Nagar 2', 'Versova Marg', 'DN Nagar', 'D.N. Nagar', 'Shri Swami Samarth Nagar', 'Millat Nagar', 'Gilbert Hill JJC', 'SV Patel Nagar', 'Shastri Nagar D Phase', 'Navneeth Colony', 'Sundervan Complex', 'Dattaguru nagar', 'Andheri East', 'Marol', 'Chakala', 'Marol Naka', 'Saki Vihar Road', 'JB Nagar', 'Poonam Nagar', 'Marol Maroshi Road', 'Asalfa Village JJC', 'Sher E Punjab Society', 'Sakinaka Junction', 'Kadam Wadi Marol', 'Seepz Area', 'Chakala MIDC', 'Dr Charatsingh Colony', 'Malpa Dongri', 'Gondavali Gaothan', 'Sahar Village', 'Kajuwadi', 'Marol Maroshi', 'PMGP Colony', 'Customs Colony', 'Mogra Village Road', 'Kanti Nagar', 'Bamandaya Pada', 'Koladongri', 'Mogra Village', 'Jijamata Road', 'Hanuman Nagar', 'Azad Nagar JJC', 'Parsi Wada', 'Marol Naka Junction', 'Bhavani Nagar', 'Maheshwari Nagar', 'Kondivita Village']
    )

data_p2 = data_p2[['ID', 'Possession Status', 'Price (English)', 'Area Name', 'Floor Data', 'Units Available', 'Covered Area', 'Price per square feet', 'Property BHK Type', 'Description/Amenities']]
data_p2.columns = ['ID', 'Possession Status', 'Cost', 'Location', 'Floor', 'Units Available', 'Flat Size (sqft)', 'Price per square feet ', 'Property BHK Type', 'Description/Amenities']

data_p4 = data_p2.copy()

base = r'^{}'
expr = '(?=.*{})'
amenities_option = base.format(''.join(expr.format(w) for w in amenities_options))
location_pref = '|'.join(location_pref)

if(len(amenities_option) != 0):
    data_p3 = data_p2[data_p2['Description/Amenities'].str.contains(amenities_option, case=False)]
    data_p3.reset_index(drop=True, inplace=True)
    data_p4 = data_p3.copy()
else:
    data_p3 = data_p2.copy()
    data_p4 = data_p2.copy()

if(len(location_pref) != 0):
    data_p4 = data_p3[data_p3['Location'].str.contains(location_pref, case=False)]
    data_p4.reset_index(drop=True, inplace=True)

print(data_p4.shape)
st.write(data_p4.drop(['Description/Amenities'], axis=1))

def convert_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

csv = convert_to_csv(data_p4)

download1 = st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='prop_list_df.csv',
    mime='text/csv'
)