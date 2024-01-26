function faceDetection() {
  console.log('faceDetection');
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 1000);
  });

  //code for face detection
   const canvas = document.getElementById('canvas');
   const ctx = canvas.getContext('2d');
   ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
   const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
   const faces = faceapi.detectAllFaces(imgData);
   ctx.clearRect(0, 0, canvas.width, canvas.height);
   faces.forEach((face) => {
     ctx.beginPath();
     ctx.arc(face.x, face.y, face.width / 2, 0, 2 * Math.PI);
     ctx.fillStyle = '#FF0000';
     ctx.fill();
     ctx.closePath();
   });

}

function clearCanvas() {
  console.log('clearCanvas');
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 1000);
  });

  //code for Canvas clear
   const canvas = document.getElementById('canvas');
   const ctx = canvas.getContext('2d');
   ctx.clearRect(0, 0, canvas.width, canvas.height);


  }

  function saveCanvas() {
  console.log('saveCanvas');
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 1000);
  });

  //code for Canvas save
   const canvas = document.getElementById('canvas');
   canvas.toBlob((blob) => {
     const url = URL.createObjectURL(blob);
     const a = document.createElement('a');
     a.href = url;
     a.download = 'canvas.png';
     a.click();
   });
  }

  function loadCanvas() {
  console.log('loadCanvas');
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 1000);
  });
  //code for Canvas load
   const canvas = document.getElementById('canvas');
   canvas.toBlob((blob) => {
     const url = URL.createObjectURL(blob);
     const a = document.createElement('a');
     a.href = url;
     a.download = 'canvas.png';
     a.click();
   });

  }

function loadImage() {
  console.log('loadImage');
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve();
    }, 1000);
  });
  //code for Image load
   const canvas = document.getElementById('canvas');
   canvas.toBlob((blob) => {
     const url = URL.createObjectURL(blob);
     const a = document.createElement('a');
     a.href = url;
     a.download = 'canvas.png';
     a.click();
   });

  }
