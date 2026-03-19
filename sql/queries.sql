
-- Create table
CREATE TABLE sales (
    total_sales FLOAT,
    tip_amount FLOAT,
    sex VARCHAR(10),
    smoker VARCHAR(10),
    day VARCHAR(10),
    time VARCHAR(10),
    customer_count INT
);

-- 1. Total sales by day
SELECT day, SUM(total_sales) AS total_revenue
FROM sales
GROUP BY day
ORDER BY total_revenue DESC;

-- 2. Average tip percentage by time
SELECT time, AVG(tip_amount / total_sales * 100) AS avg_tip_percentage
FROM sales
GROUP BY time;

-- 3. Top 5 highest sales
SELECT *
FROM sales
ORDER BY total_sales DESC
LIMIT 5;

-- 4. Customer behavior (avg spend per group size)
SELECT customer_count, AVG(total_sales) AS avg_spending
FROM sales
GROUP BY customer_count
ORDER BY customer_count;

-- 5. Smoking vs non-smoking revenue
SELECT smoker, SUM(total_sales) AS revenue
FROM sales
GROUP BY smoker;
