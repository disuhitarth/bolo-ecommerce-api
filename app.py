import streamlit as st
import requests
import json

# Function to send the API request
def send_api_request(data):
    # Set the API endpoint URL
    api_url = "https://your-api-endpoint.com"

    # Send the POST request
    response = requests.post(api_url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        st.success("API request successful!")
        st.code(response.json(), language="json")
    else:
        st.error(f"API request failed with status code: {response.status_code}")
        st.code(response.text, language="json")

# Streamlit app
def main():
<<<<<<< HEAD
    st.image("images/boloprint high.png", caption="BoloPrint Logo", width=15, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
=======
    st.title("Boloprint Marketplace API")

    # Sidebar for selecting platforms
    st.sidebar.title("Select Platforms")
    platforms = st.sidebar.multiselect("Platforms", ["etsy", "ebay", "walmart", "amazon", "shopify", "tiktok"])

    # Main area for input fields and controls
    if platforms:
        action = st.radio("Select Action", ["Add Product", "Edit Product", "Manage Order"])

        # Add Product
        if action == "Add Product":
            st.header("Add Product")
            api_token = st.text_input("API Token")

            # Common product details
            st.subheader("Common Product Details")
            title = st.text_input("Title")
            description = st.text_area("Description")
            categories = st.text_input("Categories (comma-separated)")
            tags = st.text_input("Tags (comma-separated)")
            images = st.text_input("Image URLs (comma-separated)")
            variants = st.text_input("Variants (JSON format)")
            price = st.number_input("Price")
            sale_price = st.number_input("Sale Price (optional)")
            inventory = st.number_input("Inventory")

            # Shipping profile
            st.subheader("Shipping Profile")
            weight = st.number_input("Weight")
            length = st.number_input("Length")
            width = st.number_input("Width")
            height = st.number_input("Height")

            # Platform-specific details
            for platform in platforms:
                st.subheader(f"{platform.capitalize()} Specific Details")
                if platform == "etsy":
                    who_made = st.selectbox("Who Made", ["i_did", "collective", "someone_else"])
                    is_supply = st.checkbox("Is Supply")
                    material_details = st.text_input("Material Details (JSON format)")
                    renewal_options = st.text_input("Renewal Options (JSON format)")
                elif platform == "ebay":
                    condition = st.selectbox("Condition", ["new", "used", "refurbished"])
                    condition_description = st.text_area("Condition Description")
                    returns_accepted = st.checkbox("Returns Accepted")
                    refund_option = st.selectbox("Refund Option", ["moneyBack", "moneyBackOrExchange"], disabled=not returns_accepted)
                    refund_period = st.number_input("Refund Period (days)", disabled=not returns_accepted)
                    shipping_cost = st.number_input("Shipping Cost for Returns", disabled=not returns_accepted)
                elif platform == "walmart":
                    brand = st.text_input("Brand")
                    manufacturer = st.text_input("Manufacturer")
                    model_number = st.text_input("Model Number")
                    warranty_type = st.selectbox("Warranty Type", ["manufacturer", "seller"])
                    warranty_length = st.number_input("Warranty Length (months)")
                    warranty_description = st.text_area("Warranty Description")
                elif platform == "amazon":
                    bullet_points = st.text_input("Bullet Points (comma-separated)")
                    package_length = st.number_input("Package Length")
                    package_width = st.number_input("Package Width")
                    package_height = st.number_input("Package Height")
                    package_weight = st.number_input("Package Weight")
                    hsn = st.text_input("Harmonized System Number (HSN)")
                    tsn = st.text_input("Terapeak Style Number (TSN)")
                elif platform == "shopify":
                    vendor = st.text_input("Vendor")
                    product_type = st.text_input("Product Type")
                    metafields = st.text_input("Metafields (JSON format)")
                elif platform == "tiktok":
                    video_url = st.text_input("Video URL")
                    hashtags = st.text_input("Hashtags (comma-separated)")
                    influencer_id = st.text_input("Influencer ID")

            # Submit button
            if st.button("Add Product"):
                for platform in platforms:
                    data = {
                        "action": "addProduct",
                        "marketplace": platform,
                        "apiToken": api_token,
                        "commonProductDetails": {
                            "title": title,
                            "description": description,
                            "categories": categories.split(","),
                            "tags": tags.split(","),
                            "images": images.split(","),
                            "variants": json.loads(variants),
                            "price": price,
                            "salePrice": sale_price,
                            "inventory": inventory
                        },
                        "shippingProfile": {
                            "weight": weight,
                            "dimensions": {
                                "length": length,
                                "width": width,
                                "height": height
                            }
                        }
                    }

                    # Add platform-specific details
                    if platform == "etsy":
                        data["etsySpecificDetails"] = {
                            "whoMade": who_made,
                            "isSupply": is_supply,
                            "materialDetails": json.loads(material_details),
                            "renewalOptions": json.loads(renewal_options)
                        }
                    elif platform == "ebay":
                        data["ebaySpecificDetails"] = {
                            "condition": condition,
                            "conditionDescription": condition_description,
                            "returnPolicy": {
                                "returnsAccepted": returns_accepted,
                                "refundOption": refund_option,
                                "refundPeriod": refund_period if returns_accepted else None,
                                "shippingCost": shipping_cost if returns_accepted else None
                            }
                        }
                    elif platform == "walmart":
                        data["walmartSpecificDetails"] = {
                            "brand": brand,
                            "manufacturer": manufacturer,
                            "modelNumber": model_number,
                            "warranty": {
                                "warrantyType": warranty_type,
                                "warrantyLength": warranty_length,
                                "warrantyDescription": warranty_description
                            }
                        }
                    elif platform == "amazon":
                        data["amazonSpecificDetails"] = {
                            "bulletPoints": bullet_points.split(","),
                            "packageDimensions": {
                                "length": package_length,
                                "width": package_width,
                                "height": package_height,
                                "weight": package_weight
                            },
                            "hsn": hsn,
                            "tsn": tsn
                        }
                    elif platform == "shopify":
                        data["shopifySpecificDetails"] = {
                            "vendor": vendor,
                            "productType": product_type,
                            "metafields": json.loads(metafields)
                        }
                    elif platform == "tiktok":
                        data["tiktokSpecificDetails"] = {
                            "videoUrl": video_url,
                            "hashtags": hashtags.split(","),
                            "influencerId": influencer_id
                        }

                    send_api_request(data)

        # Edit Product
        elif action == "Edit Product":
            st.header("Edit Product")
            api_token = st.text_input("API Token")
            product_id = st.text_input("Product ID")

            # Common product details
            st.subheader("Common Product Details")
            title = st.text_input("Title")
            description = st.text_area("Description")
            categories = st.text_input("Categories (comma-separated)")
            tags = st.text_input("Tags (comma-separated)")
            images = st.text_input("Image URLs (comma-separated)")
            variants = st.text_input("Variants (JSON format)")
            price = st.number_input("Price")
            sale_price = st.number_input("Sale Price (optional)")
            inventory = st.number_input("Inventory")

            # Shipping profile
            st.subheader("Shipping Profile")
            weight = st.number_input("Weight")
            length = st.number_input("Length")
            width = st.number_input("Width")
            height = st.number_input("Height")

            # Platform-specific details
            for platform in platforms:
                st.subheader(f"{platform.capitalize()} Specific Details")
                # Add platform-specific details for editing products

            # Submit button
            if st.button("Edit Product"):
                for platform in platforms:
                    data = {
                        "action": "editProduct",
                        "marketplace": platform,
                        "apiToken": api_token,
                        "productId": product_id,
                        "commonProductDetails": {
                            "title": title,
                            "description": description,
                            "categories": categories.split(","),
                            "tags": tags.split(","),
                            "images": images.split(","),
                            "variants": json.loads(variants),
                            "price": price,
                            "salePrice": sale_price,
                            "inventory": inventory
                        },
                        "shippingProfile": {
                            "weight": weight,
                            "dimensions": {
                                "length": length,
                                "width": width,
                                "height": height
                            }
                        }
                    }

                    # Add platform-specific details for editing products

                    send_api_request(data)

        # Manage Order
        else:
            st.header("Manage Order")
            api_token = st.text_input("API Token")
            # order_id = st.text_input("Order ID")
            sub_action = st.selectbox("Sub-Action", ["Download Unfulfilled Orders", "Download Order", "Update Order Status"])

            # Download Unfulfilled Orders
            if sub_action == "Download Unfulfilled Orders":
                # Submit button
                if st.button("Download Unfulfilled Orders"):
                    unfulfilled_orders = []
                    for platform in platforms:
                        data = {
                            "action": "manageOrder",
                            "subAction": "downloadUnfulfilledOrders",
                            "marketplace": platform,
                            "apiToken": api_token
                        }

                        response_data = send_api_request(data)
                        if response_data:
                            unfulfilled_orders.extend(response_data.get("unfulfilledOrders", []))

                # Display unfulfilled orders
                st.subheader("Unfulfilled Orders")
                unfulfilled_orders_str = "\n".join([f"Order ID: {order['orderId']}, Platform: {order['marketplace']}" for order in unfulfilled_orders])
                unfulfilled_orders_display = st.text_area("", unfulfilled_orders_str, height=300)

                # Fulfill order
                order_to_fulfill = st.text_input("Order ID to Fulfill")
                tracking_number = st.text_input("Tracking Number")

                if st.button("Fulfill Order"):
                    for platform in platforms:
                        data = {
                            "action": "manageOrder",
                            "subAction": "fulfillOrder",
                            "marketplace": platform,
                            "apiToken": api_token,
                            "orderId": order_to_fulfill,
                            "trackingNumber": tracking_number
                        }

                        send_api_request(data)
            # Download Order
            elif sub_action == "Download Order":
                order_id = st.text_input("Order ID")

                # Customer details
                st.subheader("Customer Details")
                name = st.text_input("Name")
                email = st.text_input("Email")
                address_line1 = st.text_input("Address Line 1")
                address_line2 = st.text_input("Address Line 2")
                city = st.text_input("City")
                state = st.text_input("State")
                zip_code = st.text_input("ZIP Code")
                country = st.text_input("Country")

                # Platform-specific details
                for platform in platforms:
                    st.subheader(f"{platform.capitalize()} Specific Details")
                    # Add platform-specific details for downloading orders

                # Submit button
                if st.button("Download Order"):
                    for platform in platforms:
                        data = {
                            "action": "manageOrder",
                            "subAction": "downloadOrder",
                            "marketplace": platform,
                            "apiToken": api_token,
                            "orderId": order_id,
                            "customerDetails": {
                                "name": name,
                                "email": email,
                                "shippingAddress": {
                                    "addressLine1": address_line1,
                                    "addressLine2": address_line2,
                                    "city": city,
                                    "state": state,
                                    "zipCode": zip_code,
                                    "country": country
                                },
                                "billingAddress": {
                                    "addressLine1": address_line1,
                                    "addressLine2": address_line2,
                                    "city": city,
                                    "state": state,
                                    "zipCode": zip_code,
                                    "country": country
                                }
                            }
                        }

                        # Add platform-specific details for downloading orders

                        send_api_request(data)

            # Update Order Status
            elif sub_action == "Update Order Status":
                order_id = st.text_input("Order ID")
                order_status = st.selectbox("Order Status", ["pending", "processing", "shipped", "delivered", "cancelled"])
                tracking_number = st.text_input("Tracking Number")

                # Customer details
                st.subheader("Customer Details")
                name = st.text_input("Name")
                email = st.text_input("Email")
                address_line1 = st.text_input("Address Line 1")
                address_line2 = st.text_input("Address Line 2")
                city = st.text_input("City")
                state = st.text_input("State")
                zip_code = st.text_input("ZIP Code")
                country = st.text_input("Country")

                # Platform-specific details
                for platform in platforms:
                    st.subheader(f"{platform.capitalize()} Specific Details")
                    if platform == "etsy":
                        message_to_seller = st.text_area("Message to Seller")
                        shipping_method_code = st.text_input("Shipping Method Code")
                    # Add other platform-specific details for updating order status

                # Submit button
                if st.button("Update Order Status"):
                    for platform in platforms:
                        data = {
                            "action": "manageOrder",
                            "subAction": "updateOrderStatus",
                            "marketplace": platform,
                            "apiToken": api_token,
                            "orderId": order_id,
                            "orderStatus": order_status,
                            "trackingNumber": tracking_number,
                            "customerDetails": {
                                "name": name,
                                "email": email,
                                "shippingAddress": {
                                    "addressLine1": address_line1,
                                    "addressLine2": address_line2,
                                    "city": city,
                                    "state": state,
                                    "zipCode": zip_code,
                                    "country": country
                                },
                                "billingAddress": {
                                    "addressLine1": address_line1,
                                    "addressLine2": address_line2,
                                    "city": city,
                                    "state": state,
                                    "zipCode": zip_code,
                                    "country": country
                                }
                            }
                        }

                        # Add platform-specific details for updating order status
                        if platform == "etsy":
                            data["etsySpecificDetails"] = {
                                "messageToSeller": message_to_seller,
                                "shippingMethodCode": shipping_method_code
                            }

                        send_api_request(data)
            
    else:
        st.warning("Please select at least one platform.")

if __name__ == "__main__":
    main()
