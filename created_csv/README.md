# Created CSV Files

This folder contains several CSV files generated during the customer segmentation analysis. Below is a brief description of each file:

## Files

1. **transaction_df.csv**
   - **Description**: This file contains transaction data for each customer.
   - **Columns**:
     - `customer_id`: Unique identifier for each customer.
     - `age`: Age of the customer.
     - `gender`: Gender of the customer.
     - `item_purchased`: Name of the item purchased.
     - `category`: Category of the item purchased.
     - `purchase_amount_(usd)`: Amount spent in the transaction.
     - `location`: Location of the customer.
     - `size`: Size of the item purchased.
     - `color`: Color of the item purchased.
     - `season`: Season during which the purchase was made.
     - `review_rating`: Review rating given by the customer.
     - `subscription_status`: Subscription status of the customer.
     - `shipping_type`: Type of shipping chosen.
     - `discount_applied`: Whether a discount was applied.
     - `promo_code_used`: Whether a promo code was used.
     - `previous_purchases`: Number of previous purchases made by the customer.
     - `payment_method`: Payment method used.
     - `frequency_of_purchases`: Frequency of purchases made by the customer.
     - `product_id`: Product ID (first occurrence).

2. **product_df.csv**
   - **Description**: This file contains information about the products.
   - **Columns**:
     - `item_purchased`: Name of the product.
     - `color`: Color of the product.
     - `category`: Category of the product.
     - `average_purchase_amount`: Average purchase amount for the product.
     - `average_review_rating`: Average review rating for the product.
     - `has_discount`: Whether the product has a discount.
     - `product_id`: Unique identifier for each product.

3. **customer_cluster_{cluster_id}_df.csv**
   - **Description**: This file contains customer data for a specific cluster. `{cluster_id}` should be replaced with the actual cluster number.
   - **Columns**:
     - `customer_id`: Unique identifier for each customer.
     - `age`: Age of the customer.
     - `gender`: Gender of the customer.
     - `total_purchase_amount`: Total amount spent by the customer.
     - `location`: Location of the customer.
     - `total_purchases`: Total number of purchases made by the customer.
     - `is_subscriber`: Whether the customer is a subscriber.
     - `preferred_size`: Preferred size of the customer.
     - `preferred_color`: Preferred color of the customer.
     - `preferred_shipping`: Preferred shipping method of the customer.
     - `used_promo_code`: Whether the customer used a promo code.
     - `preferred_payment_method`: Preferred payment method of the customer.
     - `average_review_rating`: Average review rating given by the customer.
     - `average_purchase_amount`: Average purchase amount per transaction.
     - `cluster`: Cluster label assigned to the customer.

4. **customer_feature_importance.csv**
   - **Description**: This file contains the importance of each feature in predicting the cluster labels, as determined by a RandomForestClassifier.
   - **Columns**:
     - `feature`: Name of the feature.
     - `importance`: Importance score of the feature.

## Usage

These CSV files can be used for further analysis and visualization of customer segments. They provide insights into the characteristics of each cluster and the importance of different features in determining the clusters.