CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE offset_value INT;
    SET offset_value=N-1;
    RETURN (
        Select distinct salary from employee 
        order by salary desc 
        limit offset_value,1

    );
END