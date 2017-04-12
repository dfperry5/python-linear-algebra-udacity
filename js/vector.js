module.exports = {
    constants: {
        CANNOT_NORMALIZE_ZERO_VECTOR_MSG: 'Cannot normalize Zero Vector'
    },

    plus: function(v1, v2){
        var sum = v1.map((num, idx) =>
        {
            return num + v2[idx];
        });
        return sum;
    },

    minus: (v1,v2) =>
        {
            var difference = v1.map((num, idx) => {
                return num - v2[idx];
            })
            return difference;
        }

}
