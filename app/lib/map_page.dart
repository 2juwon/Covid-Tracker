import 'package:flutter/material.dart';
import 'package:naver_map_plugin/naver_map_plugin.dart';

class MapPage extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Naver Map'),
      ),
      body: NaverMap(
        initialCameraPosition: CameraPosition(
          target: LatLng(35.22662, 128.87227),
          zoom: 17,
        ),
        initLocationTrackingMode:
        LocationTrackingMode.NoFollow,
        mapType: MapType.Basic,
      ),
    );
  }
}
