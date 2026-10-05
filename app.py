import streamlit as st
import math

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Textile Count & CV% Calculator",
    page_icon="🧵",
    layout="centered"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🧵 Textile Count Calculator")
st.write("Calculate yarn count and CV% easily.")

st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------
tab1, tab2 = st.tabs([
    "🧵 Count Calculator",
    "📊 CV% Calculator"
])

# ==================================================
# TAB 1 - COUNT CALCULATOR
# ==================================================
with tab1:

    st.subheader("Yarn Count Calculator")

    calculation_type = st.selectbox(
        "Select Calculation",
        [
            "Calculate Count from Length & Weight",
            "Convert Count"
        ]
    )

    # --------------------------------------------------
    # COUNT FROM LENGTH AND WEIGHT
    # --------------------------------------------------
    if calculation_type == "Calculate Count from Length & Weight":

        st.write("Enter the yarn/fiber length and weight.")

        system = st.selectbox(
            "Select Count System",
            [
                "English Count (Ne)",
                "Metric Count (Nm)",
                "Tex",
                "Denier"
            ]
        )

        col1, col2 = st.columns(2)

        with col1:
            length = st.number_input(
                "Length",
                min_value=0.0,
                value=0.0,
                step=1.0
            )

        with col2:
            weight = st.number_input(
                "Weight",
                min_value=0.0,
                value=0.0,
                step=0.1
            )

        if system == "English Count (Ne)":
            length_unit = st.selectbox(
                "Length Unit",
                ["yards", "meters"]
            )

            weight_unit = st.selectbox(
                "Weight Unit",
                ["pounds", "grams"]
            )

        elif system == "Metric Count (Nm)":
            length_unit = st.selectbox(
                "Length Unit",
                ["meters", "yards"]
            )

            weight_unit = st.selectbox(
                "Weight Unit",
                ["grams", "kilograms", "pounds"]
            )

        else:
            length_unit = st.selectbox(
                "Length Unit",
                ["meters", "yards"]
            )

            weight_unit = st.selectbox(
                "Weight Unit",
                ["grams", "kilograms", "pounds"]
            )

        if st.button("Calculate Count", type="primary"):

            if length <= 0 or weight <= 0:
                st.error("Please enter valid length and weight values.")

            else:

                try:

                    # ------------------------------------------
                    # ENGLISH COUNT (Ne)
                    # ------------------------------------------
                    if system == "English Count (Ne)":

                        # Convert length to yards
                        if length_unit == "meters":
                            length_yards = length * 1.0936133
                        else:
                            length_yards = length

                        # Convert weight to pounds
                        if weight_unit == "grams":
                            weight_pounds = weight * 0.00220462262
                        else:
                            weight_pounds = weight

                        # Ne = Length in yards / (840 × weight in pounds)
                        count = length_yards / (840 * weight_pounds)

                        st.success(f"English Count (Ne) = **{count:.2f}**")

                    # ------------------------------------------
                    # METRIC COUNT (Nm)
                    # ------------------------------------------
                    elif system == "Metric Count (Nm)":

                        # Convert length to meters
                        if length_unit == "yards":
                            length_meters = length * 0.9144
                        else:
                            length_meters = length

                        # Convert weight to grams
                        if weight_unit == "kilograms":
                            weight_grams = weight * 1000
                        elif weight_unit == "pounds":
                            weight_grams = weight * 453.59237
                        else:
                            weight_grams = weight

                        # Nm = length in meters / weight in grams
                        count = length_meters / weight_grams

                        st.success(f"Metric Count (Nm) = **{count:.2f}**")

                    # ------------------------------------------
                    # TEX
                    # ------------------------------------------
                    elif system == "Tex":

                        # Tex = weight in grams / length in meters × 1000
                        if length_unit == "yards":
                            length_meters = length * 0.9144
                        else:
                            length_meters = length

                        if weight_unit == "kilograms":
                            weight_grams = weight * 1000
                        elif weight_unit == "pounds":
                            weight_grams = weight * 453.59237
                        else:
                            weight_grams = weight

                        tex = (weight_grams / length_meters) * 1000

                        st.success(f"Tex = **{tex:.2f}**")

                    # ------------------------------------------
                    # DENIER
                    # ------------------------------------------
                    elif system == "Denier":

                        # Denier = weight in grams / length in meters × 9000
                        if length_unit == "yards":
                            length_meters = length * 0.9144
                        else:
                            length_meters = length

                        if weight_unit == "kilograms":
                            weight_grams = weight * 1000
                        elif weight_unit == "pounds":
                            weight_grams = weight * 453.59237
                        else:
                            weight_grams = weight

                        denier = (weight_grams / length_meters) * 9000

                        st.success(f"Denier = **{denier:.2f}**")

                except ZeroDivisionError:
                    st.error("Weight and length must be greater than zero.")

    # --------------------------------------------------
    # COUNT CONVERSION
    # --------------------------------------------------
    else:

        st.write("Convert one yarn count system into another.")

        source_system = st.selectbox(
            "From",
            [
                "English Count (Ne)",
                "Metric Count (Nm)",
                "Tex",
                "Denier"
            ]
        )

        source_value = st.number_input(
            "Enter Count",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        target_system = st.selectbox(
            "Convert To",
            [
                "English Count (Ne)",
                "Metric Count (Nm)",
                "Tex",
                "Denier"
            ]
        )

        if st.button("Convert Count", type="primary"):

            if source_value <= 0:
                st.error("Please enter a count greater than zero.")

            elif source_system == target_system:
                st.info(f"{source_system} = **{source_value:.2f}**")

            else:

                # First convert source to Tex
                if source_system == "English Count (Ne)":
                    tex_value = 590.541 / source_value

                elif source_system == "Metric Count (Nm)":
                    tex_value = 1000 / source_value

                elif source_system == "Tex":
                    tex_value = source_value

                elif source_system == "Denier":
                    tex_value = source_value / 9

                # Then convert Tex to target
                if target_system == "English Count (Ne)":
                    result = 590.541 / tex_value

                elif target_system == "Metric Count (Nm)":
                    result = 1000 / tex_value

                elif target_system == "Tex":
                    result = tex_value

                elif target_system == "Denier":
                    result = tex_value * 9

                st.success(
                    f"{source_value:.2f} {source_system} = "
                    f"**{result:.2f} {target_system}**"
                )

# ==================================================
# TAB 2 - CV% CALCULATOR
# ==================================================
with tab2:

    st.subheader("CV% Calculator")

    st.write(
        "Enter multiple test readings separated by commas."
    )

    data_input = st.text_area(
        "Enter Values",
        placeholder="Example: 20.1, 20.4, 19.8, 20.2, 20.0"
    )

    if st.button("Calculate CV%", type="primary"):

        if not data_input.strip():
            st.error("Please enter some values.")

        else:

            try:

                # Convert entered values into numbers
                values = [
                    float(value.strip())
                    for value in data_input.split(",")
                    if value.strip()
                ]

                if len(values) < 2:
                    st.error("Please enter at least two values.")

                elif any(value < 0 for value in values):
                    st.error("Values cannot be negative.")

                else:

                    # Mean
                    mean = sum(values) / len(values)

                    if mean == 0:
                        st.error(
                            "Mean is zero, so CV% cannot be calculated."
                        )

                    else:

                        # Sample standard deviation
                        variance = sum(
                            (value - mean) ** 2
                            for value in values
                        ) / (len(values) - 1)

                        standard_deviation = math.sqrt(variance)

                        # CV%
                        cv = (
                            standard_deviation / mean
                        ) * 100

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric(
                                "Number of Readings",
                                len(values)
                            )

                        with col2:
                            st.metric(
                                "Mean",
                                f"{mean:.3f}"
                            )

                        with col3:
                            st.metric(
                                "CV%",
                                f"{cv:.2f}%"
                            )

                        st.success(
                            f"Coefficient of Variation (CV%) = "
                            f"**{cv:.2f}%**"
                        )

                        st.write(
                            "Standard Deviation = "
                            f"**{standard_deviation:.3f}**"
                        )

            except ValueError:
                st.error(
                    "Invalid input. Please enter numbers separated by commas."
                )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "Textile Count & CV% Calculator | Streamlit Web Application"
)
