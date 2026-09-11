# E-Commerce Sales Exploratory Data Analysis
An end-to-end exploratory data analysis (EDA) of e-commerce transaction data, focusing on revenue performance, product categories, temporal trends, customer spending behavior, and customer satisfaction.

## Interactive Dashboard Features
The repository includes a live Streamlit application (`app.py`) for interactive data exploration:

* **Sidebar Category Filtering:** Multi-select widget to filter all key performance indicators and visualizations dynamically.
* **Executive KPI Cards:** Real-time calculation of Total Revenue, Total Orders, and Average Order Value based on active filters.
* **2x2 Visual Analytics Grid:**
  * **Category Revenue Breakdown:** Seaborn bar plot showing aggregate sales by product department.
  * **Price vs. Rating Dynamics:** Regression plot displaying customer rating distributions relative to price points.
  * **Category Rating Distributions:** Box plot showing satisfaction score spread and medians across departments.
  * **Monthly Revenue Performance:** Multi-color grouped bar chart breaking down monthly revenue trends by category.

**Live Interactive Dashboard:** 
[https://ecommerce-sales-eda-4g2rwnfatwbmaaycqnuypc.streamlit.app/](https://ecommerce-sales-eda-4g2rwnfatwbmaaycqnuypc.streamlit.app/)
## Dataset Overview

The dataset contains 441 sanitized e-commerce sales records covering transactional, customer, demographic, and product information.

| Feature           | Type    | Description                                  |
| :---------------- | :------ | :------------------------------------------- |
| `order_id`        | String  | Unique transaction identifier                |
| `customer_name`   | String  | Customer name                                |
| `date`            | String  | Transaction date                             |
| `month`           | String  | Month associated with the transaction        |
| `gender`          | String  | Customer demographic (`Male`, `Female`, `-`) |
| `category`        | String  | Product category                             |
| `price`           | Float   | Unit price of the product                    |
| `quantity`        | Integer | Quantity purchased                           |
| `sales`           | Float   | Total order value (`price × quantity`)       |
| `customer_rating` | Float   | Customer review score on a 0–10 scale        |

## Key Findings & Business Insights

### Category Revenue

Grocery generated the highest total revenue at **$125,421.98**, representing approximately **18.8%** of total revenue. Clothing and Electronics followed with approximately 16.4% and 15.4%, respectively.

### Data Quality

The `Not Known` category accounted for approximately **12.8% of total revenue ($85,577.59)**. This indicates a significant category-labeling issue that could affect category-level reporting and suggests a need for improved data validation upstream in the pipeline.

### Price and Customer Satisfaction

Correlation analysis found essentially **no linear relationship between product price and customer rating** (`r ≈ -0.00`). Within this dataset, higher-priced products were therefore not associated with lower customer satisfaction.

### Customer Spending

Customer-level aggregation was used to identify high-value customers based on total spending, order frequency, and average order value (AOV). These metrics can help identify customers who may be valuable targets for retention and engagement strategies.

## Analysis Performed

The analysis explores:

* Revenue by product category
* Monthly revenue trends
* Revenue distribution across customer genders and categories
* Customer rating distributions by category
* Relationship between product price and customer ratings
* Customer spending and order-level behavior
* Data quality issues affecting category classification

## Technologies Used

* Python 3.9+ , pandas, Numpy, Matplotlib, Seaborn, Jupyter Notebook, streamlit


## Getting Started

Clone the repository:

```bash
    git clone https://github.com/Ibrahim-katama/ecommerce-sales-eda.git
    cd ecommerce-sales-eda
```

Install the required dependencies:

```bash
    pip install -r requirements.txt
```

Open the analysis notebook:

```bash
    jupyter notebook sales_analysis.ipynb
```
Or Launch the interactive dashboard directly using bash:
```bash
    streamlit run app.py
```
Then open `sales_analysis.ipynb` and run the cells sequentially to reproduce the analysis, visualizations, and statistical results.

## Data Privacy

The dataset used in this project has been sanitized for analysis and does not contain real customer information.