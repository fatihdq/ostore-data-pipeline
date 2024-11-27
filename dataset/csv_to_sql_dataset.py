import pandas as pd


transformMap = [
    {
        "input": "./dataset/raw/olist_products_dataset.csv",
        "output": "./dataset/postgres/1_products_insert.sql",
        "table": "products",
        "dtypes": {
            "product_id": str,
            "product_category_name": str,
            "product_name_lenght": int,	
            "product_description_lenght": int,
            "product_photos_qty": int,
            "product_weight_g": int,
            "product_length_cm": int,
            "product_height_cm": int,
            "product_width_cm": int,
        }
    },
    {
        "input": "./dataset/raw/olist_customers_dataset.csv",
        "output": "./dataset/postgres/2_customers_insert.sql",
        "table": "customers",
        "dtypes": {
            "customer_id": str,
            "customer_unique_id": str,
            "customer_zip_code_prefix": int,
            "customer_city": str,
            "customer_state": str,
        }
    },
    {
        "input": "./dataset/raw/olist_geolocation_dataset.csv",
        "output": "./dataset/postgres/3_geolocations_insert.sql",
        "table": "geolocations",
        "dtypes": {
            "geolocation_zip_code_prefix": str,
            "geolocation_lat": float,
            "geolocation_lng": float,
            "geolocation_city": str,
            "geolocation_state": str,
        }
    },
    {
        "input": "./dataset/raw/olist_sellers_dataset.csv",
        "output": "./dataset/postgres/4_sellers_insert.sql",
        "table": "sellers",
        "dtypes": {
            "seller_id": str,
            "seller_zip_code_prefix": str,
            "seller_city": str,
            "seller_state": str,
        }
    },
    {
        "input": "./dataset/raw/olist_orders_dataset.csv",
        "output": "./dataset/postgres/5_orders_insert.sql",
        "table": "orders",
        "dtypes": {
            "order_id": str,
            "customer_id": str,
            "order_status": str,
            "order_purchase_timestamp": str,
            "order_approved_at": str,
            "order_delivered_carrier_date": str,
            "order_delivered_customer_date": str,
            "order_estimated_delivery_date": str,
        }
    },
    {
        "input": "./dataset/raw/olist_order_payments_dataset.csv",
        "output": "./dataset/postgres/6_order_payments_insert.sql",
        "table": "order_payments",
        "dtypes": {
            "order_id": str,
            "payment_sequential": int,
            "payment_type": str,
            "payment_installments": int,
            "payment_value": float,
        }
    },
    {
        "input": "./dataset/raw/olist_order_items_dataset.csv",
        "output": "./dataset/postgres/7_order_items_insert.sql",
        "table": "order_items",
        "dtypes": {
            "order_id": str,
            "order_item_id": str,
            "product_id": str,
            "seller_id": str,
            "shipping_limit_date": str,
            "price": float,
            "freight_value": float,
        }
    },
]


for item in transformMap:
    print(item["table"])
    data = pd.read_csv(item["input"],delimiter=",",dtype=str)

    sqlInsert = f"""INSERT INTO {item["table"]} ({", ".join(data.columns)})
    VALUES """

    for i, row in data.iterrows():
        sqlValue = "("
        for j, col in enumerate(data.columns):
            if pd.isna(row[col]):
                sqlValue += " NULL"
            elif item["dtypes"][col] == str:
                sqlValue += " '"+row[col].replace("'","''")+"'"
            elif item["dtypes"][col] == int:
                sqlValue += " "+str(int(float(row[col])))
            elif item["dtypes"][col] == float:
                sqlValue += " "+str(float(row[col]))
            elif item["dtypes"][col] == bool:
                sqlValue += " "+str(row[col])
            
            if j != len(data.columns)-1:
                sqlValue += ","

        if i != len(data)-1:
            sqlValue += "),\n"
        else:
            sqlValue += ")"

        sqlInsert += sqlValue
    sqlInsert += ";"

    with open(item["output"],"w") as f:
        f.write(sqlInsert)
        f.close()