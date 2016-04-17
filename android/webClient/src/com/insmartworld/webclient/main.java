package com.insmartworld.webclient;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebChromeClient;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.Toast;
import android.webkit.SslErrorHandler;
import android.net.http.SslError;

public class main extends Activity
{
    private WebView webView;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);

        // Web View Settings
        webView = (WebView) findViewById(R.id.webView);
        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setAllowFileAccessFromFileURLs(true);
        settings.setAllowUniversalAccessFromFileURLs(true);
        settings.setBuiltInZoomControls(true);
        String StaticIP = "insmartworld.com";
        final Activity activity = this;
                
        webView.setWebViewClient(new WebViewClient() {
            public void onReceivedError(WebView view, int errorCode, String description, String failingUrl) {
                Toast.makeText(activity, description, Toast.LENGTH_SHORT).show();
            }
        });
        webView.setWebViewClient( new SSLTolerentWebViewClient() ); 
        webView.loadUrl("http://"+StaticIP+"/");
        //setContentView(R.layout.main);
    } 

    // SSL Error Tolerant Web View Client
    private class SSLTolerentWebViewClient extends WebViewClient {
        @Override
        public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error) {
            handler.proceed(); // Ignore SSL certificate errors
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        webView.loadUrl("javascript:window.location.reload(true)");
    }

    @Override
    protected void onPause() {
        super.onPause();
        webView.clearCache(false);
    }

    @Override
    protected void onStop() {
        super.onStop();
        webView.clearCache(true);
    }
}
