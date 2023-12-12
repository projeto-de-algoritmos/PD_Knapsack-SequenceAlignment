$(document).ready(function() {

  function lis(arr, n, maxRef) {
  if (n === 1)
      return 1;

  let maxEndingHere = 1;

  for (let i = 1; i < n; i++) {
      const res = lis(arr, i, maxRef);
      if (arr[i - 1] < arr[n - 1] && res + 1 > maxEndingHere)
          maxEndingHere = res + 1;
  }

  if (maxRef.max < maxEndingHere)
      maxRef.max = maxEndingHere;

  return maxEndingHere;
}

function findLIS(arr) {
  const n = arr.length;
  const maxRef = { max: 1 };
  lis(arr, n, maxRef);

  return maxRef.max;
}

$('#calculate').on('click', function(){
  var numberArray = $('#arrayList').val().split(',').map(Number);
  if($('#arrayList').val() == ""){
      Swal.fire({
          title: 'Erro!',
          text: "Por favor insira os numeros desejados separados por ,",
          icon: 'error',
          confirmButtonText: 'Calcular novos números'
      })
      return;
  }
  
  Swal.fire({
      title: 'Sucesso!',
      text: "A maior subsequencia crescente possui "+findLIS(numberArray)+" números",
      icon: 'success',
      confirmButtonText: 'Calcular novos números'
  })
})
})