export dot_product
# Created as a routine


function dot_product(A, B)

# First we multiply together the values
    for i in 1:length(A)
        A[i] *= B[i]
    end

    ans = 0
# Then we add sum them together. This produces our dot product
    for i in A
        ans += i
    end

    return ans
end
