-- =============================================
-- APPLICATION USAGE ANALYTICS PIPELINE
-- Business Intelligence Queries
-- =============================================

-- 1. Overall Adoption Summary
SELECT 
    COUNT(*) as total_records,
    ROUND(AVG(adoption_rate), 2) as avg_adoption_rate,
    ROUND(AVG(manual_rate), 2) as avg_manual_rate,
    ROUND(AVG(efficiency_score), 2) as avg_efficiency_score,
    MIN(adoption_rate) as lowest_adoption,
    MAX(adoption_rate) as highest_adoption
FROM app_usage;

-- 2. Branch-wise Performance (Key Business View)
SELECT 
    branch,
    COUNT(*) as total_entries,
    ROUND(AVG(adoption_rate), 2) as avg_adoption_pct,
    ROUND(SUM(app_tasks), 0) as total_app_tasks,
    ROUND(SUM(manual_tasks), 0) as total_manual_tasks,
    ROUND(AVG(efficiency_score), 2) as avg_efficiency,
    COUNT(CASE WHEN adoption_category = 'Excellent' THEN 1 END) as excellent_adoption_days
FROM app_usage 
GROUP BY branch
ORDER BY avg_adoption_pct DESC;

-- 3. Adoption Trend Over Time
SELECT 
    date,
    ROUND(AVG(adoption_rate), 2) as daily_avg_adoption,
    ROUND(AVG(efficiency_score), 2) as daily_efficiency
FROM app_usage 
GROUP BY date
ORDER BY date;

-- 4. Department-wise Analysis
SELECT 
    department,
    ROUND(AVG(adoption_rate), 2) as avg_adoption,
    ROUND(SUM(manual_tasks), 0) as total_manual_tasks
FROM app_usage 
GROUP BY department;

-- 5. High Impact Records (Low Adoption)
SELECT 
    employee_id,
    branch,
    adoption_rate,
    manual_rate,
    adoption_category
FROM app_usage 
WHERE adoption_rate < 70
ORDER BY adoption_rate ASC;