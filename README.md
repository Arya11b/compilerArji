# compilerArji
## Lexical Analyzer

### test case results
<table>
<thead>
<tr><th>Lexemes          </th><th>Types               </th><th>Attributes  </th></tr>
</thead>
<tbody>
<tr><td>uwu              </td><td>TOKEN_ID            </td><td>Index_ID 0  </td></tr>
<tr><td>_w_              </td><td>TOKEN_ID            </td><td>Index_ID 1  </td></tr>
<tr><td>_1234            </td><td>TOKEN_ID            </td><td>Index_ID 2  </td></tr>
<tr><td>abcd13e          </td><td>TOKEN_ID            </td><td>Index_ID 3  </td></tr>
<tr><td>abcd13_          </td><td>TOKEN_ID            </td><td>Index_ID 4  </td></tr>
<tr><td>abcd13_e_        </td><td>TOKEN_ID            </td><td>Index_ID 5  </td></tr>
<tr><td>ABCD13_e_E_ea    </td><td>TOKEN_ID            </td><td>Index_ID 6  </td></tr>
<tr><td>_                </td><td>TOKEN_ID            </td><td>Index_ID 7  </td></tr>
<tr><td>a                </td><td>TOKEN_ID            </td><td>Index_ID 8  </td></tr>
<tr><td>12345            </td><td>TOKEN_INTEGER       </td><td>12345       </td></tr>
<tr><td>0x25             </td><td>TOKEN_INTEGER       </td><td>37          </td></tr>
<tr><td>0                </td><td>TOKEN_INTEGER       </td><td>0           </td></tr>
<tr><td>0b0              </td><td>TOKEN_INTEGER       </td><td>0           </td></tr>
<tr><td>0x0              </td><td>TOKEN_INTEGER       </td><td>0           </td></tr>
<tr><td>0.0              </td><td>TOKEN_REAL          </td><td>0.0         </td></tr>
<tr><td>12.34            </td><td>TOKEN_REAL          </td><td>12.34       </td></tr>
<tr><td>"Spire"          </td><td>TOKEN_STRING        </td><td>Spire       </td></tr>
<tr><td>"Sent"
+
	"ence."</td><td>TOKEN_STRING        </td><td>Sentence.   </td></tr>
<tr><td>.                </td><td>TOKEN_DOT           </td><td>.           </td></tr>
<tr><td>64               </td><td>TOKEN_INTEGER       </td><td>64          </td></tr>
<tr><td>64               </td><td>TOKEN_INTEGER       </td><td>64          </td></tr>
<tr><td>.                </td><td>TOKEN_DOT           </td><td>.           </td></tr>
<tr><td>.                </td><td>TOKEN_DOT           </td><td>.           </td></tr>
<tr><td>23               </td><td>TOKEN_INTEGER       </td><td>23          </td></tr>
<tr><td>24               </td><td>TOKEN_INTEGER       </td><td>24          </td></tr>
<tr><td>.                </td><td>TOKEN_DOT           </td><td>.           </td></tr>
<tr><td>320              </td><td>TOKEN_INTEGER       </td><td>320         </td></tr>
<tr><td>""               </td><td>TOKEN_STRING        </td><td>            </td></tr>
<tr><td>"
"              </td><td>TOKEN_STRING        </td><td>            </td></tr>
<tr><td>"+"              </td><td>TOKEN_STRING        </td><td>+           </td></tr>
<tr><td>.                </td><td>TOKEN_DOT           </td><td>.           </td></tr>
<tr><td>""               </td><td>TOKEN_STRING        </td><td>            </td></tr>
<tr><td>*                </td><td>TOKEN_MULTIPLICATION</td><td>*           </td></tr>
<tr><td>/                </td><td>TOKEN_DIVISION      </td><td>/           </td></tr>
<tr><td>UwU              </td><td>TOKEN_ID            </td><td>Index_ID 9  </td></tr>
<tr><td>-23              </td><td>TOKEN_INTEGER       </td><td>-23         </td></tr>
<tr><td>=                </td><td>TOKEN_ASSIGNMENT    </td><td>=           </td></tr>
<tr><td>6                </td><td>TOKEN_INTEGER       </td><td>6           </td></tr>
<tr><td>^                </td><td>TOKEN_POWER         </td><td>^           </td></tr>
<tr><td>_                </td><td>TOKEN_ID            </td><td>Index_ID 7  </td></tr>
<tr><td><                </td><td>TOKEN_LT            </td><td><           </td></tr>
<tr><td>0x1              </td><td>TOKEN_INTEGER       </td><td>1           </td></tr>
<tr><td>*                </td><td>TOKEN_MULTIPLICATION</td><td>*           </td></tr>
<tr><td>3                </td><td>TOKEN_INTEGER       </td><td>3           </td></tr>
<tr><td><<               </td><td>TOKEN_SHIFT_LEFT    </td><td><<          </td></tr>
<tr><td>_a_              </td><td>TOKEN_ID            </td><td>Index_ID 11 </td></tr>
<tr><td>;                </td><td>TOKEN_SEMICOLON     </td><td>;           </td></tr>
</tbody>
</table>

