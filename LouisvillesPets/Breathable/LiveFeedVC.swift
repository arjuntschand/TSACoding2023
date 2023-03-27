//
//  LiveFeedVC.swift
//  Breathable
//
//  Created by Arjun Tschand on 2/19/23.
//

import UIKit

class LiveFeedVC: UIViewController {

    // Initialize variables used to set image feed and status
    var returnStr:String = ""

    // Set IP address used to connect to the server
    var ip_address:String = "1.1.1.1"
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        self.getLiveData(value2: "load initial view")
        let timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { timer in
            self.getLiveData(value2: "timer")
        }
    }
    
    // Encodes base64 and sets ImageView to the content of the received graph
    // Also sets AAQS label to returned AAQS and the label color to calculated RGB of AAQS
    func getLiveData(value2: String) {
            sendRequestToServer(parameters: value2) {
                (returnval, error) in
                if (returnval)!
                {
                    // Wait for response from server before updating imageView and label
                    DispatchQueue.main.async { [self] in
                        self.StatusLabelText.text = self.returnStr.components(separatedBy: ",")[0]
                        self.StatusLabelText.textColor = UIColor(red: ((NumberFormatter().number(from: (self.returnStr.components(separatedBy: ",")[1])) as! CGFloat)/1), green: ((NumberFormatter().number(from: (self.returnStr.components(separatedBy: ",")[2])) as! CGFloat)/1), blue: 0, alpha: 1)
                        let newImageData = Data(base64Encoded: self.returnStr.components(separatedBy: ",")[3])
                        ImageView.image = UIImage(data: newImageData!)
                        self.TimestampLabel.text = "Last Updated @ " +  self.returnStr.components(separatedBy: ",")[4]
                    }
                } else {
                    print(error)
                }
            }
            DispatchQueue.main.async { // Correct
            }
        }
        
        // Sends HTTP request to the server with request for most recent concentrations and their respective RGB
        func sendRequestToServer(parameters: String, CompletionHandler: @escaping (Bool?, Error?) -> Void){
            let json = [parameters]
            do {
                let jsonData = try JSONSerialization.data(withJSONObject: json, options: .prettyPrinted)
                
                
                let url = NSURL(string: "http://" + ip_address + ":5001/liveFeed")!
                let request = NSMutableURLRequest(url: url as URL)
                request.httpMethod = "Get"
                
                request.setValue("application/json; charset=utf-8", forHTTPHeaderField: "Content-Type")
                
                // Send HTTP request to the server
                let task = URLSession.shared.dataTask(with: request as URLRequest){ [self] data, response, error in
                    if let returned = String(data: data!, encoding: .utf8) {
                        print(returned)
                        self.returnStr = returned
                        
                        CompletionHandler(true,nil)
                    } else {
                    }
                }
                task.resume()
            } catch {
                print(error)
            }
        }

    @IBOutlet weak var StatusLabelText: UILabel!
    @IBOutlet weak var ImageView: UIImageView!
    @IBOutlet weak var TimestampLabel: UILabel!
}
