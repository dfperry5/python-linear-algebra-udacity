// module.exports = {
//     constants: {
//         CANNOT_NORMALIZE_ZERO_VECTOR_MSG: 'Cannot normalize Zero Vector'
//     },

//     plus: function(v1, v2){
//         var sum = v1.map((num, idx) =>
//         {
//             return num + v2[idx];
//         });
//         return sum;
//     },

//     minus: (v1,v2) => {
//         var difference = v1.map((num, idx) => {
//             return num - v2[idx];
//         })
//         return difference;
//     },

//     times_scalar: (v1, scalar) => {
//         let result = v1.map( (num, idx) => {
//             return num * scalar
//         })
//         return result;
//     }

// }

class Vector {

    // constants: {
    //     CANNOT_NORMALIZE_ZERO_VECTOR_MSG: 'Cannot normalize Zero Vector'
    // },
    constructor(x) {
        this.coordinates = x;
    }

    toString(){
        let str = '[ ' ;
        this.coordinates.forEach( (num, idx) => {
            str += num;
            if(idx < this.coordinates.length -1 ){
                str +=  ", ";
            }
        });
        str += ' ]';
        return str;
    }

    plus(v2){
        var sum = this.coordinates.map((num, idx) =>
        {
            return num + v2.coordinates[idx];
        });
        return new Vector(sum);
    }

    minus(v2){
        var difference = this.coordinates.map((num, idx) => {
            return num - v2.coordinates[idx];
        })
        return new Vector(difference);
    }

    times_scalar(scalar){
        let result = this.coordinates.map( (num, idx) => {
            return num * scalar
        })
        return new Vector(result);
    }
};

module.exports = Vector;