## Comparisons vs. Functions

1. Improve the following query

```
SELECT count(*)
FROM shawarma_purchases
WHERE
  YEAR(purchased_at) == '2017'
```
