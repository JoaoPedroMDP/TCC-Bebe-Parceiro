import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RemoveInformationComponent } from './remove-information.component';

describe('RemoveInformationComponent', () => {
  let component: RemoveInformationComponent;
  let fixture: ComponentFixture<RemoveInformationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RemoveInformationComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RemoveInformationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
