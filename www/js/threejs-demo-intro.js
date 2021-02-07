const aspect_ratio = window.innerWidth / window.innerHeight;
const clock = new THREE.Clock();

let animation_mixer = undefined;
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
   25,
   aspect_ratio,
   0.1,
   100,
);
camera.position.x = 15;
camera.position.y = -5;
camera.position.z = 15;
camera.lookAt(0,0,0);

const renderer = new THREE.WebGLRenderer();
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFShadowMap;
renderer.shadowMap.renderSingleSided = false;
renderer.setClearColor(new THREE.Color("0xFFFFFF"));
const container = document.getElementById("canvas_container");
container.appendChild(renderer.domElement);

let demo_obj = undefined;
const gltf_obj_loader = new THREE.GLTFLoader();
gltf_obj_loader.load(
   "/3d/tommygons/test_demo.glb",
   (gltf_obj) => {
      scene.add(gltf_obj.scene);
      gltf_obj.scene.traverse(obj => {
         obj.castShadow = true;
         obj.receiveShadow = true;
      });
      demo_obj = gltf_obj.scene;
      console.log(demo_obj);
      gltf_obj.scene.scale.set(1, 1, 1);
      gltf_obj.scene.castShadow = true;
      gltf_obj.scene.receiveShadow = true;
      animation_mixer = new THREE.AnimationMixer(gltf_obj.scene);
   },
   () => {},
   ( error ) => { console.error( error ); },
);


const lights = [];
lights[0] = new THREE.SpotLight(
   0xffff00,
   1.0,
   0.0,
   Math.PI / 12,
   0.0,
   0.0,
);
lights[1] = new THREE.SpotLight(
   0xFFFFFF,
   1.0,
   0,
   Math.PI / 3,
   0,
   0,
);
lights[0].position.set(0, 2, 5);
lights[1].position.set(0, 0, 15);
const spotlight_target = new THREE.Object3D(0, -1, 0);
const origin = new THREE.Object3D(0, 0, 0);
lights[0].target = scene;
lights[1].target = scene;
lights[0].castShadow = true;
lights[0].receiveShadow = true;
lights[0].shadow.mapSize.width = 4096;
lights[0].shadow.mapSize.height = 4096;
lights[0].shadow.bias =  -0.0001;
lights[0].shadow.radius = 0.01;
lights[0].shadow.camera.near = 0.05;
lights[0].shadow.camera.far = 15;
lights[1].castShadow = true;
lights[1].receiveShadow = true;
lights[1].shadow.mapSize.width = 4096;
lights[1].shadow.mapSize.height = 4096;
lights[1].shadow.bias = -0.0001;
lights[1].shadow.radius = 25;
lights[1].shadow.camera.near = 1;
lights[1].shadow.camera.far = 20;
// lights[0].shadow.focus = 2;
const spotlight_helper = new THREE.SpotLightHelper(lights[0]);
// scene.add(lights[0]);
scene.add(lights[1]);
scene.add(spotlight_target);
// scene.add(spotlight_helper);

const cube_group = new THREE.Group();
const cube_geometry = new THREE.BoxGeometry();
const cube_lineMaterial = new THREE.LineBasicMaterial(
   {
      color: 0x00F0F0,
      transparent: true,
      opacity: 1.00,
      // linecap: "round",  // Ignored by WebGL Rendering Engine
      // linewidth: 1,      // Ignored by WebGL Rendering Engine
   }
);
const cube_material = new THREE.MeshPhongMaterial(
   {
      color: 0x00FF00,
      emissive: 0x000000,
      wireframe: false,
      flatShading: false,
   }
);
cube_group.add(new THREE.Mesh(cube_geometry, cube_material));
// cube_group.add(new THREE.LineSegments(cube_geometry, cube_lineMaterial));
// scene.add(cube_group);

const background_geometry = new THREE.PlaneGeometry(40, 40, 1, 1);
const background_lineMaterial = new THREE.LineBasicMaterial(
   {
      color: 0x00F0F0,
      transparent: true,
      opacity: 1.00,
      // linecap: "round",  // Ignored by WebGL Rendering Engine
      // linewidth: 1,      // Ignored by WebGL Rendering Engine
   }
);
const background_material = new THREE.MeshPhongMaterial(
   {
      color: 0x00F990,
      // emissive: 0x000000,
      // wireframe: false,
      side: THREE.DoubleSide,
      flatShading: true,
   }
);
const background_group = new THREE.Group();
background_group.add(new THREE.Mesh(background_geometry, background_material));
// background_group.add(new THREE.LineSegments(background_geometry, background_lineMaterial));
background_group.position.z = -5.1;
background_group.traverse(obj => {
   obj.castShadow = false;
   obj.receiveShadow = true;
});
background_group.castShadow = false;
background_group.receiveShadow = true;
console.log(background_group);
scene.add(background_group);

const plane_geometry = new THREE.PlaneGeometry(5, 5, 1, 1);
const plane_lineMaterial = new THREE.LineBasicMaterial(
   {
      color: 0x00F0F0,
      transparent: true,
      opacity: 1.00,
      // linecap: "round",  // Ignored by WebGL Rendering Engine
      // linewidth: 1,      // Ignored by WebGL Rendering Engine
   }
);
const plane_material = new THREE.MeshPhongMaterial(
   {
      color: 0xF99090,
      // emissive: 0x000000,
      // wireframe: false,
      side: THREE.DoubleSide,
      // flatShading: true,
   }
);
const plane_group = new THREE.Group();
plane_group.add(new THREE.Mesh(plane_geometry, plane_material));
// plane_group.add(new THREE.LineSegments(plane_geometry, plane_lineMaterial));
plane_group.position.z = -5;
plane_group.traverse(obj => {
   obj.castShadow = false;
   obj.receiveShadow = true;
});
plane_group.castShadow = false;
plane_group.receiveShadow = true;
console.log(plane_group);
scene.add(plane_group);

function resizeCanvasToDisplaySize() {
   const canvas = renderer.domElement;
   // look up the size the canvas is being displayed
   const width = canvas.clientWidth;
   const height = canvas.clientHeight;

   // adjust displayBuffer size to match
   if (canvas.width !== width || canvas.height !== height) {
      // you must pass false here or three.js sadly fights the browser
      renderer.setSize(width, height, false);
      camera.aspect = width / height;
      camera.updateProjectionMatrix();

      // update any render target sizes here
   }
}



let updateCameraPosition = function hstUpdateCameraPosition(new_z) {
   camera.position.z = new_z;
   return;
}

const btn_camera_z_out = document.querySelector("#camera_z_up")
const btn_camera_z_in = document.querySelector("#camera_z_dn")

btn_camera_z_out.addEventListener("click", () => {updateCameraPosition(Math.max(camera.position.z + 5, 0))});
btn_camera_z_in.addEventListener("click", () => {updateCameraPosition(Math.max(camera.position.z - 5, 0))});


let frame_count = 0;
let step_move = 0.025;

const animate = function () {
   resizeCanvasToDisplaySize();

   // cube_group.rotation.x += 0.01;
   // cube_group.rotation.y += 0.01;

   // camera.position.x -= 0.015;

   // lights[0].position.x -= 0.025;
   lights[0].position.y = Math.sin(2 * Math.PI * frame_count / 50);
   // spotlight_target.position.x -= 0.025;
   spotlight_target.position.y = Math.sin(2 * Math.PI * frame_count / 50);
   if (frame_count == 0)
   {
      // lights[0].position.x = 5;
      // spotlight_target.position.x = 5;
      // camera.position.x = 3;
   }
   spotlight_helper.update();

   frame_count = (frame_count + 1) % 400;

   if (demo_obj) {
      demo_obj.position.z = 4 * Math.sin(2 * Math.PI * frame_count / 200);
      demo_obj.rotation.x += 0.01;
   }

   if (animation_mixer) {
      animation_mixer.update(clock.getDelta());
   }

   renderer.render(scene, camera);

   requestAnimationFrame(animate);
};

animate();
