import 'package:flutter/material.dart';
import 'geolocator_page.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _userIDCon = TextEditingController();
  final _userPWCon = TextEditingController();

  dynamic userID;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blueAccent,
        centerTitle: true,
        titleTextStyle: const TextStyle(fontWeight: FontWeight.bold, fontStyle: FontStyle.italic, color: Colors.black12),
        title: const Text('나의 동선 체크하기'),
      ),
      body: _buildBody(),
    );
  }

  Widget _buildBody() {
    return SafeArea(
      child: ListView(
        children: <Widget>[
          const Padding(padding: EdgeInsets.all(50.0)),
          Image.network('https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbLPiSf%2Fbtq1beLDyUT%2F7fXnWzSbZq2nEnqbQyKSmk%2Fimg.jpg', fit: BoxFit.fill),
          const Padding(padding: EdgeInsets.all(50.0)),
          TextField(
            controller: _userIDCon,
            decoration: const InputDecoration(
              filled: true,
              labelText: 'User ID',
              labelStyle: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
            ),
          ),
          TextField(
            controller: _userPWCon,
            decoration: const InputDecoration(
              filled: true,
              labelText: 'User Password',
              labelStyle: TextStyle(fontSize: 16.0, fontWeight: FontWeight.bold),
            ),
            obscureText: true,
          ),
          ButtonBar(
            children: <Widget>[
              IconButton(
                onPressed: () {
                  userID = _userIDCon.text;
                  _checkUser(userID);
                },
                icon: const Icon(Icons.login, color: Colors.black),
                tooltip: 'Login',
              ),
            ],
          ),
        ],
      ),
    );
  }

  void _checkUser(String iD) {
    if (iD != '') {
      if (iD == 'shlee') {
        Navigator.push(context, MaterialPageRoute(builder: (BuildContext) => const MainPage()));
      } else {
        // ID, PW 초기화
        setState(() {
          _userIDCon.clear();
          _userPWCon.clear();
        });
      }
    }
  }
}

