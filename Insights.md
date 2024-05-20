# Insights from Superstore Data Analysis
For a detailed review of the analysis, please refer to the [Jupyter notebook](eda_retail.ipynb).

## Key Findings

1. **Category Analysis**:
   - The `Furniture` category has higher total sales but a lower average profit compared to `Office Supplies`.
   - The `Technology` category, has the highest sales as well as the highest average profit.

2. **Sub-Category Analysis**:
   - The `Phones` sub-category has the highest total sales, followed by `Chairs` and `Storage`.
   - The `Copiers` sub-category has the highest average profit, indicating a very profitable product line.
   - The `Furnishings` and `Paper` sub-categories have relatively high average profits but lower total sales.
   - The `Tables`, `BookCases`, and `Supplies` sub-category has negative average profit, suggesting it is a loss-making product line.

3. **Regional Analysis**:
   - The `West` region has the highest total sales as well as average profit among all regions.
   - The `East` region has the second-highest total sales and average profit, trailing closely behind the West region.
   - The `Central` region has the lowest average profit among all regions, despite having the third-highest total sales.
   - The `South` region has the lowest total sales among all regions but has relatively higher average profit.

4. **Segment Analysis**:
   - The `Consumer` segment has the highest total sales among the three segments.
   - The `Home Office` segment has the lowest total sales compared to the other two segments.
   - In terms of average profit, the Home `Office segment` has the highest value, outperforming the `Corporate` and `Consumer` segments.
   - The `Corporate` segment has the second-highest average profit, trailing behind the `Home Office` segment.
The `Consumer segment`, despite having the highest total sales, has the lowest average profit among the three segments.

5. **Shipping Mode Analysis**:
   - `Standard Class` is the most used shipping mode but has a lower average profit.
   - `First Class` and `Same Day` shipping modes, although used less frequently, have higher average profits.

7. **State Analysis**:
   - `California` has the highest total sales among all states.
   - `New York` has the second-highest total sales and one of the highest average profit.
   - `Texas` and `Pennsylvania` have relatively high total sales but negative average profit.
   - `Washington` and `Michigan` have lower total sales but among the highest average profit.
   - Several states, including `Ohio`, `Illinois`, and `Colorado`, have moderate to high total sales but negative average profit.
   - Some states with relatively low total sales, such as `Vermont`, `Rhode Island`, and `Delaware`, have exceptionally high average profit.
   - A few states, like `Florida` and `Oregon`, have moderate total sales but slightly negative average profit.
   - Certain states with lower total sales, such as `Wyoming` and `South Dakota`, have relatively high average profit.
   - There is a wide range in total sales and average profit across different states, highlighting regional variations in performance.

6. **Discount Impact Analysis**:
   - There is a negative correlation between discount and profit, indicating that higher discounts generally reduce profit margins.

## Recommendations

Based on the key findings, here are some recommendations:

1. **Category and Sub-Category Optimization**:
   - Focus on expanding the product offerings in the highly profitable `Technology` category.
   - Evaluate the pricing and cost structure of the `Furniture` category to improve profitability.
   - Consider phasing out or restructuring the loss-making sub-categories like `Tables`, `Bookcases`, and `Supplies`.
   - Leverage the high-profit sub-categories like `Copiers` and `Phones` as growth drivers.

2. **Regional Strategy**:
   - Concentrate efforts on maintaining and growing market share in the high-performing `West` and `East` regions.
   - Identify opportunities to improve profitability in the `Central` region, potentially through cost optimization or pricing adjustments.
   - Explore strategies to boost sales in the `South` region, leveraging its relatively higher profitability.

3. **Segment Focus**:
   - Prioritize the `Home Office` segment, as it has the highest average profit margin, while also exploring ways to increase sales in this segment.
   - Evaluate the pricing and cost structure of the `Consumer` segment to improve profitability, given its high sales volume.
   - Consider targeted marketing and product strategies for the `Corporate` segment to capitalize on its moderate profitability.

4. **Shipping Mode Optimization**:
   - Incentivize customers to choose more profitable shipping modes like `First Class` and `Same Day` by offering competitive pricing or bundling with other services.
   - Evaluate the cost structure and pricing strategy for `Standard Class` shipping to improve profitability.

5. **State-level Optimization**:
   - Concentrate efforts on maintaining and growing market share in high-performing states like `California`, `New York`, `Washington`, and `Michigan`.
   - Identify opportunities to improve profitability in states like `Texas`, `Pennsylvania`, `Ohio`, `Illinois`, and `Colorado`, potentially through cost optimization or pricing adjustments.
   - Explore strategies to boost sales in states with relatively low total sales but high average profit, such as `Vermont`, `Rhode Island`, and `Delaware`.

6. **Discount Strategy**:
   - Review the discount strategy and consider limiting or optimizing discounts to maintain profitability.
   - Explore alternative promotional strategies that do not heavily rely on discounting.

7. **Data-driven Decision Making**:
   - Leverage the available data and insights to make informed decisions regarding product portfolio management, pricing strategies, resource allocation, and targeted marketing efforts.
   - Continuously monitor and analyze sales and profitability data to identify emerging trends and opportunities for improvement.
